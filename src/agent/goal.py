"""
    Goal class
    This describes and stores (sub-)goals and their relationships
    Types,
        Conjunctive: achieving both sub goal A and B can attain the parent goal
        Disjunctive: achieving more than one of the sub goals satisfies attainment of the parent goal

    States of a goal
-----------------------------------------------------
STATE        | TRIGGER                  | NEXT_STATE
=====================================================
NOT_ASSIGNED | more than one agent      | ASSIGNED
             | is assigned              |
-----------------------------------------------------
ASSIGNED     | start conditions are met | ACTIVE
-----------------------------------------------------
ACTIVE       | end conditions are met   | ACHIEVED
             | ????                     | FAILED
-----------------------------------------------------

"""
GOAL_STATE_NOT_ASSIGNED = 'not_assigned'
GOAL_STATE_ASSIGNED = 'assigned'
GOAL_STATE_ACTIVE = 'active'
GOAL_STATE_ACHIEVED = 'achieved'
GOAL_STATE_FAILED = 'failed'

'''
    Create a goal from a given description
    Format:
        <<goal>>::<<goal_name>>
                  <<require>>
                  <<trigger>>
                  <<satisfy>>
                  <<precedent>>
        <<require>>::<<task>>
                     <<goal>>
        <<trigger>>::<<knowledge>>
        <<satisfy>>::<<knowledge>>
    example: {
        'goal': 'say hello',
        'trigger': [],
        'satisfy':
        'require': [['say', 'hello']]}
'''
def create_goal_set(description_dict):
    assert 'goal' in description_dict

    g = Goal(description_dict['goal'])
    if 'trigger' in description_dict:
        g.set_triggers(description_dict['trigger'])
    if 'satisfies' in description_dict:
        g.set_satisfies(description_dict['satisfies'])
    if 'require' in description_dict:
        dependents = description_dict['require']
        for dependent in dependents:
            if isinstance(dependent, list):  # Task
                g.set_required_task(Task(dependent[0], dependent[1]))
            elif isinstance(dependent, dict): # Goal
                g.set_required_goal(create_goal_set(dependent))
            else:
                pass
    else:
        # A goal with no tasks that satisfy it
        return None

    return g


class Goal(object):
    def __init__(self, goal_name=''):
        self.name = goal_name
        self.tasks = []
        self.dependents = []
        self.triggers = []
        self.satisfies = []
        self.goal_state = GOAL_STATE_NOT_ASSIGNED

    def __repr__(self):
        return '%s with %s tasks and %s dependents' % (self.name, self.tasks, self.dependents)

    def _get_leaf_tasks(self):
        if len(self.dependents) == 0:
            return self.tasks
        else:
            for dependent in self.dependents:
                if dependent.goal_state != GOAL_STATE_ACHIEVED and dependent.goal_state != GOAL_STATE_FAILED:
                    return dependent._get_leaf_tasks()
            return self.tasks

    def set_goal_name(self, goal_name):
        self.name = goal_name

    def set_required_task(self, task):
        self.tasks.append(task)

    def set_required_goal(self, goal):
        self.dependents.append(goal)

    def set_triggers(self, triggers):
        self.triggers = triggers

    def set_satisfies(self, satisfies):
        self.satisfies = satisfies

    def get_tasks(self):
        return self.tasks

    def get_available_tasks(self):
        tasks = self._get_leaf_tasks()
        return tasks

    # Modified self.goals -> self.dependents
    def get_goal(self):
        if len(self.dependents) > 0:
            return self.dependents[0]
        else:
            return None

class Task(object):
    def __init__(self, task_name='', arguments={}):
        self.__name__ = task_name
        self.arguments = arguments

    def __repr__(self):
        return '[Task \'%s\' with \'%s\']' % (self.__name__, self.arguments)

    def set_arguments(self, arguments):
        self.arguments = arguments
