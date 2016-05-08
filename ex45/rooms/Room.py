class Room(object):
    '''The base room
    
    Sets up common things for all rooms'''
    
    def __init__(self):
        self.narrate()
    
    def narrate(self):
        print self.__doc__
        
    def get_action(self, prompt):
        self.action = raw_input(prompt)
        return self.action
        
    def kill_hero(self, killed_by):
        print "\n\nDEATH EMBRACES YOU.\nYou were killed by %s!" % killed_by
        exit(-1)