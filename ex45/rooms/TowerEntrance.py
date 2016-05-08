from Room import Room

class TowerEntrance(Room):
    '''The Tower's Entrance
    
    You make your way to the tower entrance by moonlight and arrive to see a
    single disheveled troll standing guard at the mighty wooden door. You smell
    his stench from where you're crouched in the bushes a crossbow bolt's flight
    away. He's large, very large, wearing loincloth and a leather harness from
    which tiny human skulls hang. He's keeping himself busy eating a torn off 
    deer leg.
    
    You think you might be able to get a shot off with your crossbow, or maybe 
    sap him. You know a direct engagement is unwise.
    '''
    
    def __init__(self):
        print self.__doc__
        self.treasures = []
        
    def run(self):
        next = self.get_action('How do you approach to get past the troll?\n> ')
        
        if 'sap' in next and 'sneak' not in next:
            self.kill_hero('the trolls inside who heard their buddy\'s skull go THWACK! and rushed out to clobber you')
        elif 'sap' in next and 'sneak' in next:
            print 'You sneak up to the poor bastard and buttstroke him with your crossbow. He slumps over, dropping his dinner.'
        elif 'shoot' in next or 'bolt' in next or 'crossbow' in next:
            print 'Good idea. You take aim and let loose a bolt. It buries itself in the troll\'s forehead and he falls, twitching for a few seconds before laying still.'
        else: 
            print "Oh no, %s doesn't cut it! The troll's attention is directed to you and you've been found out!" % next.lower()
            self.kill_hero('the guardian toll\'s alertness and appetite!')
            
        next = self.get_action('The door is locked. How do you get inside?\n> ')
        
        successful_actions = ['pick the lock', 'take the keys', 'steal the keys', 'find the keys', 'search for the keys']
        
        for action in successful_actions:
            if action in next:
                print "You quietly and smoothly %s before you're found out. That seems to have worked! The door creaks open." % action.lower()
                return 'TowerLevelOne'
        
        # oh shit nothing worked!
        print "Oh no, you can't %s in time before you're seen by a troll scout party!" % action.lower()
        self.kill_hero('the troll scout party bum rushing you')