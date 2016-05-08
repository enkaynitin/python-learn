from Room import Room

class TowerLevelOne(Room):
    '''The Tower Level 1
    
    You creak open the door and sneak inside... and almost thump into one of
    the two trolls' chests before you notice them waiting for  you there! They
    must have heard you open the door.
    '''
    
    def __init__(self):
        print self.__doc__
        self.treasures = []
        
    def run(self):
        print "entered the first level"
        
        next = 'Think fast! One troll raises his club to pulverize you while the other cackles!\n> '
        
        if next == 'tumble between his legs':
            print """
Your mind is as nimble as your feet! You tumble through and
the troll thwacks his buddy dead! You take advantage of the 
situation and slip your dagger between the dumbfounded troll's ribs,
then help his limp body slump to the floor quietly.
            """
        else:
            print "Too slow! THWACK!"
            self.kill_hero('the troll\'s club smashing down into your skull')    
            
        print "You find the stairs and ascend to the next room."
        return 'TowerLevelTwo'