import sys

# namespace hell in DungeonRunner.run() 
# better way of doing this?
import rooms
from rooms import StartAdventure
from rooms import TowerEntrance
from rooms import TowerLevelOne
from rooms import TowerLevelTwo
from rooms import TowerLevelThree
from rooms import TowerLevelFour
from rooms import TowerLevelFive

class DungeonRunner(object):
    '''Run the dungeon.
    
    Go through it room by room and make sure the hero doesn't die!
    '''
    
    def __init__(self, run_room):
        self.run_room = run_room
        
    def run(self):
        '''Run the room
        
        Room should be a class all by itself. This is what the exercise calls
        for at http://learnpythonthehardway.org/book/ex45.html
        '''

        while True:
            # this is fugly dude. this is seriously fugly.
            # look up the class in the module and instantiate it as current_room
            current_room = getattr(getattr(rooms, self.run_room), self.run_room)()
            self.run_room = current_room.run()
            if self.run_room == '':
                exit(0)