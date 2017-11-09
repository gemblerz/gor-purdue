"""
    Knowledge base class
    This stores statements formed from observations/communications
    Atomic forms are
        type1: noun, noun/adjective                e.g., (apple, red)
        type2: noun, verb [objective]              e.g., (probe, gather, the mineral)
        type3: verb, (noun/verb noun/adjective)    e.g., (attack, (target, hurt)), (attack, (drain, my_energy))
"""

class Knowledge(object):
    def __init__(self, knowledge_type, *args):
        if knowledge_type == 'type1':
            assert len(args) == 2
            self.type = knowledge_type
            self.n = args[0]
            self.na = args[1]
            print(">> New Knowledge: %s %s %s " % (self.type, self.n, self.na))
        elif knowledge_type == 'type2':
            assert len(args) == 3
            self.type = knowledge_type
            self.n = args[0]
            self.v = args[1]
            self.o = args[2]
            print(">> New Knowledge: %s %s %s %s " % (self.type, self.n, self.v, self.o))
        elif knowledge_type == 'type3':
            pass
        else:
            # unknown type
            pass


    def __str__(self):
        if self.type == 'type1':
            return self.n + " " + str(self.na)
        elif self.type == 'type2':
            return self.n + " " + self.v + " " + str(self.o)
        else:
            return "unknown type"


    """
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    """

