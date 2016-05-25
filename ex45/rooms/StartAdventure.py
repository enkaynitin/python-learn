from Room import Room

class StartAdventure(Room):
    '''Gitzold's Tale
    
    You sit back in your chair in the tavern staring at Gitzold's messy beard 
    as he tells his pitiful story of being a great arcanist researching
    alchemical advances for His Majesty, but having his tower overrun by a
    band of dirty, filthy trolls. What's a "great arcanist" without his tower
    anyway? Through his ramblings, you gather that he left the scrolls with
    all of the discoveries he has made in this tower of his, but that the new
    residents of the tower are far too powerful to even consider taking it
    back by force.
    
    "That's why you're here," the disheveled old mage sternly points out. "You
    must go in there without being discovered and find my scrolls!"
    '''
    
    def __init__(self):
        print self.__doc__
        # sorry, no treasures in the tavern
        self.treasures = []
        
    def run(self):
        next = self.get_action('Do you have any questions for Gitzold?\n> ')
        
        if 'yes' in next:
            print 'Gitzold lowers his gaze and looks at you over his glasses\n"Yes? What is your question?"'
            next = self.get_action('Gitzold is expecting a question\n> ')
            
        if 'how many trolls' in next:
            print 'Gitzold sighs and says, "I don\'t know, there must be at least ten."'
        elif 'when' in next and 'start' in next:
            print 'Gitzold grins and sends you on your way'
        else: 
            print 'Gitzold nods and sends you on your way'

        return 'TowerEntrance'