#!/usr/bin/python3

"""
    This is a core module that supports fundamental componets to run simulation.
"""

import logging
import threading
import os
import time
import sys
sys.path.append('../agent')
from agent import Agent
from goal import Goal, create_goal_set

from sc2_comm import sc2
from s2clientprotocol import sc2api_pb2 as sc_pb
from s2clientprotocol import raw_pb2 as raw_pb

from utils.communicator import Communicator, proxy

FORMAT = '%(asctime)s %(module)s %(levelname)s %(lineno)d %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

class Core(object):

    def __init__(self):
        self.comm_sc2 = sc2()
        self.port = 5000

        if sys.platform == "darwin": # Mac OS X
            self.launcher_path = "/Applications/StarCraft\ II/Support/SC2Switcher.app/Contents/MacOS/SC2Switcher\
                                  --listen 127.0.0.1\
                                  --port %s"%self.port
            self.map_path = os.getcwd()+'/../../resource/Maps/GorasMap.SC2Map'

        elif sys.platform == "win32": # Windows
            pass
            #self.launcher_path =
            #self.map_path =

        else:
            logger.error("Sorry, we cannot start on your OS.")

        # Communicator between the core and agents.
        self.comm_agents = Communicator(core=True)

        # Set the Proxy and Agents Threads.
        self.thread_proxy=threading.Thread(target=proxy)
        self.threads_agents=[]

    def init(self):

        # execute SC2 client.
        try:
            os.system(self.launcher_path)

            time.sleep(5) # need time to connect after launch app.

        except:
            logger.error("Failed to open sc2.")

        #connection between core and sc2_client using sc2 protobuf.
        self.comm_sc2.open()

    def deinit(self):
        pass

    def _start_new_game(self):

        # create a game
        try:
            map_info = sc_pb.LocalMap()

            map_info.map_path = self.map_path
            create_game = sc_pb.RequestCreateGame(local_map=map_info)
            create_game.player_setup.add(type=1)
            # create_game.player_setup.add(type=2)

            create_game.realtime = True

            # send Request
            print(self.comm_sc2.send(create_game=create_game))
            # print (test_client.comm.read())

            logger.info('New game is created.')
        except Exception as ex:
            logger.error('While creating a new game: %s'%str(ex))

        # join the game
        try:
            interface_options = sc_pb.InterfaceOptions(raw=True, score=True)
            join_game = sc_pb.RequestJoinGame(race=3, options=interface_options)

            # send Request
            print(self.comm_sc2.send(join_game=join_game))

            logger.info('Success to join the game.')
        except Exception as ex:
            logger.error('While joining the game: %s'%str(ex))

        # Game Start
        try:
            print(self.comm_sc2.send(step=sc_pb.RequestStep(count=1)))

            logger.info('Game is Started.')
        except Exception as ex:
            logger.error('While starting a new game: %s'%str(ex))

    def _start_proxy(self):
        logger.info("Try to turn on proxy...")
        self.thread_proxy.start()
        time.sleep(1) # wait for turn on proxy

    def train_probe(self, nexus_tag):
        unit_command = raw_pb.ActionRawUnitCommand(ability_id=1006)
        unit_command.unit_tags.append(nexus_tag)
        action_raw = raw_pb.ActionRaw(unit_command=unit_command)
        action = sc_pb.RequestAction()
        action.actions.add(action_raw=action_raw)
        self.comm_sc2.send(action=action)
        observation = sc_pb.RequestObservation()
        t = self.comm_sc2.send(observation=observation)

        return  t.observation.observation.raw_data.units[-1].tag

    def request_amount_of_mules(self):
        observation = sc_pb.RequestObservation()
        t = self.comm_sc2.send(observation=observation)

        #print(t.observation.observation.player_common.minerals)
        return t.observation.observation.player_common.minerals

    def run(self):

        self._start_new_game()
        self._start_proxy()

        list_mineral_tag = []
        list_agent_tag = []
        nexus_tag = []

        observation = sc_pb.RequestObservation()
        t = self.comm_sc2.send(observation=observation)

        for unit in t.observation.observation.raw_data.units:
            if unit.unit_type == 84:  # Probe unit_type_tag
                list_agent_tag.append(unit.tag)
            if unit.unit_type == 341:  # Mineral unit_type_tag
                list_mineral_tag.append(unit.tag)
            if unit.unit_type == 59:
                nexus_tag.append(unit.tag)

        print(list_agent_tag)

        goal = {'goal': 'gather 100 minerals',
                'trigger': [],
                'satisfy': [
                    ('type2', 'i', 'have', ['100 minerals'])
                ],
                'precedent': [],
                'require': [
                    ['move', {'target': 'point', 'pos_x': 10, 'pos_y': 10}],
                    ['gather', {'target': 'unit','unit_tag':list_mineral_tag[0]}],  # target: unit
                ]

                }

        probe = Agent()

        probe.spawn(list_agent_tag[0], 84,
                    initial_knowledge=[
                        ('type1', 'my_name', ['probe']),
                        ('type2', 'i', 'have', ['0 minerals']),
                    ],
                    initial_goals=[create_goal_set(goal)]
                    )
        self.threads_agents.append(probe)

        print('Agent is running...')
        try:
            self.threads_agents[0].start()
            """
                
                #build_pylon
                unit_command = raw_pb.ActionRawUnitCommand(ability_id=881)
                unit_command.unit_tags.append(list_unit_tag[0])
                unit_command.target_world_space_pos.x = 38
                unit_command.target_world_space_pos.y = 29
                action_raw = raw_pb.ActionRaw(unit_command=unit_command)
                action = sc_pb.RequestAction()
                action.actions.add(action_raw=action_raw)
                self.comm.send(action=action)
                time.sleep(2)
                
                
                #train_probe test
                unit_command = raw_pb.ActionRawUnitCommand(ability_id=1006)
                unit_command.unit_tags.append(nexus[0])
                action_raw = raw_pb.ActionRaw(unit_command=unit_command)
                action = sc_pb.RequestAction()
                action.actions.add(action_raw=action_raw)
                self.comm.send(action=action)
                time.sleep(2)
            """


        except KeyboardInterrupt:
            pass

        while True:
            self.request_amount_of_mules()
            time.sleep(10)


        # Wait for all threads exit
        for threads in self.threads_agents:
            threads.join()

        probe.destroy()
        self.comm_agents.context.term()


        print('The agent is terminated.')


if __name__ == '__main__':
    core = Core()
    logger.info('Core initializing...')
    core.init()
    logger.info('Core running...')
    core.run()
    logger.info('Core deinitializing...')
    core.deinit()
    logger.info('Core terminated.')