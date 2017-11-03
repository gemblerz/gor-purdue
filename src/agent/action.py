
from s2clientprotocol import sc2api_pb2 as sc_pb
from s2clientprotocol import raw_pb2 as raw_pb
"""
    Action class
    This lists all possible actions of a unit
    Actions can be performed under conditions and events
"""


'''
    Returns basic acitons of an agent
'''
def get_basic_actions():
    actions = []
    code = '''
self.tell(words)
    '''
    actions.append(Action(action_name='say', actual_code=code, require={'words': 'string'}))
    return actions


class Action(object):
    def __init__(self, action_name, actual_code, require={}, sc_action_id=9999):
        self.__name__ = action_name
        self.code = actual_code
        self.sc2_id = sc_action_id
        self.require = require

    def __repr__(self):
        return 'Action %s with id %d requires %s ' % (self.__name__, self.sc2_id, self.require)

    def set_arguments(self, args):
        self.require=args

    def can_perform(self, task_name):
        if task_name == self.__name__:
            return True
        else:
            return False

    def perform(self, spawn_id):
        # Pass arguments
        print(self)
        unit_command = raw_pb.ActionRawUnitCommand(ability_id=self.sc2_id)
        unit_command.unit_tags.append(spawn_id)

        if self.require['target'] == 'point':
            unit_command.target_world_space_pos.x = self.require['pos_x']
            unit_command.target_world_space_pos.y = self.require['pos_y']

        elif self.require['target'] == 'unit':
            unit_command.target_unit_tag = self.require['unit_tag']
        else:
            pass

        action_raw = raw_pb.ActionRaw(unit_command=unit_command)
        action = sc_pb.RequestAction()
        action.actions.add(action_raw=action_raw)

        return action
        # Perform the action in real


