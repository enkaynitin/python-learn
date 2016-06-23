#modules
from sys import exit
import random
import pickle
import os
import time

def new_line():
    print "\n"


#################   G A M E   D E S C R I P T I O N   ####################################
def game_description():
    """This is a Memory Game.
    
    The Goals of this game are as follows:
    -Ability to easily add/remove new words & definitions
    -Incorporate different ways of learning
        -Studies have shown that teaching the same thing different ways
         helps to make it stick
    -Randomize order of quiz questions
    -Have the ability in the game to create Word and Definition Files to be played
        -Treat these Word and Definition Files as modules that can be loaded from 
        within the game
            -This could be done two ways:Every new set of Word/Definition lists could be
            seperate functions within the same module/.py file(Leaning towards this, not as messy...,
            but still modular), or every new set of Word/Definition lists could be seperate modules/.py files
    -Try to incorporate as much as possible from what has been taught up to this point
    in "Learn Python The Hard Way". Also go back and redo/add to the game as I progress in the book
    -Back Me Up, Back Me Up, Back Me Up to DropBox
         
    Outline:
    1. Display Words and Definitions
    2. Quiz user via Multiple Choice
    3. Quiz user via Fill in the blank
    """
    print ('Type "help the hard way" to access the game description The Hard Way.\n'
          'Type "help" to access the game description the easy way.\n'
          'To go straight into the program press Enter')
    help = raw_input("> ")
    
    if help == ("help the hard way"):
        new_line()
        print ("Run the following commands in the Python interpreter for the game "
               "description:\nimport ex36\nhelp(ex36.game_description)")
        raw_input("\nPress Enter to Continue\n"
        "> ")
        game_description()       
    elif help == ("help"):
        new_line()
        print game_description.__doc__
        raw_input("\nPress Enter to Continue\n"
        "> ")
        game_description()
    else:
        start()
##########################################################################################


#################  I N T R O D U C T I O N  ##############################################  
def start():
    print "Welcome to the ever Expandable, Modular, and Most Importantly Fascinating Memory GAME GAMe GAme Game"
    print "1. Create, Edit, or Delete a Word Set."
    print "2. Plaaaayyyyy the Game!!!"
    print "3. Exit"
    choice = raw_input("> ")
    
    if choice == ("1"):
        game_editor()
    elif choice == ("2"):
        game()
    elif choice == ("3"):
        exit(0)    
    else:
        print "That is not an option. Please type 1, 2, or 3."
        start()
##########################################################################################



#########################  G A M E    E D I T O R  #######################################
def game_editor():
    print "---G A M E  E D I T O R---"
    print "1. Create New Word Set"
    print "2. Edit Existing Word Set"
    print "3. Delete Existing Word Set"
    print "4. Return to Previous Menu"
    
    choice = raw_input("> ")
        
    if choice == ("1"):
        game_editor_create()
    elif choice == ("2"):
        game_editor_edit()
    elif choice == ("3"):
        game_editor_delete()
    elif choice == ("4"):
        start()
    else:
        print "That is not an option. Please type 1, 2, 3, or 4."
        game_editor()
            
            
def game_editor_create():
    words = {}
    print "Game Editor Word Set Creator"
    print "Enter the name for the New Word Set."
    print "*Warning* If you enter the name of an exisiting Word Set, it will be overwritten!"
    words_name = raw_input("> ")
    display_purposes_only = words_name
    dictionary_filename = (words_name + ".pickle")
    print '"%s" has been created. You will now enter words followed by their definitions.' % words_name
    print 'To finish creating a new list type "DONE" for the Word *and* Definition fields.'
    words_name = words # This turns words_name into a blank dictionary, see the first line in this function.
    
    word = "not DONE"
    definition = "not DONE"
    while (word and definition != "DONE"):
        word = raw_input("Word> ")
        print word    
        
        definition = raw_input("Definition> ")
        print definition
        words_name.update({word:definition})
        
        print words_name
    
        if word and definition == "DONE":
            words_name.pop("DONE") #this pop and the next one take the "DONE" off the list :)
            print '\n\n\n"%s"' % display_purposes_only
            print words_name
            print "\n"
            with open(dictionary_filename, 'wb') as handle:
                pickle.dump(words_name, handle)
            game_editor()
    
    
def game_editor_edit():
    print "Game Editor Word Set Editor"
    print "Enter the name of the Word Set you wish to Edit."
    game_file = raw_input("> ")
    display_purposes_only = game_file
    dictionary_filename = (game_file + ".pickle")
    with open(dictionary_filename, 'rb') as handle:
        words_name = pickle.load(handle)
    print '"%s" will now be displayed. Enter words you wish to edit or add followed by their definitions.' % game_file
    print words_name
    print 'To finish editing the list type "DONE" for the Word *and* Definition fields.'
    
    word = "not DONE"
    definition = "not DONE"
    while (word and definition != "DONE"):
        word = raw_input("Word> ")
        print word    
        
        definition = raw_input("Definition> ")
        print definition
        words_name.update({word:definition})
        
        print words_name
    
        if word and definition == "DONE":
            words_name.pop("DONE") # this pop takes "DONE" off the list
            print '\n\n\n"%s"' % display_purposes_only
            print words_name
            print "\n"
            with open(dictionary_filename, 'wb') as handle:
                pickle.dump(words_name, handle)
            game_editor()

def game_editor_delete():
    print "Game Editor Word Set Deletor"
    print "Enter the name of the Word Set you wish to Delete."
    delete_set = raw_input("> ")
    delete_set_corrected = (delete_set + ".pickle") 
    # previous line has an added benefit of Only allowing the program to delete .pickle files, it can't just willy nilly delete any file
    try:
        os.remove(delete_set_corrected)
        print '"%s" has been deleted' % delete_set
    except:
        print "File not found"

    game_editor()

##########################################################################################

# Go BACK through all code and turn duplicated code into functions...


#########################  G A M E  ######################################################
# See game_description doc string for where/how I want the word/definition lists to stored
# Eventually Make A couple Switches so that when I run ex45.py from the command line I could
# run it as python ex45.py game test -- "game" would tell it to go straight to game mode
# and test would be the name of the file I want to play.

def game():
    print "----G A M E----"
    print "1. Auto Practice Mode"
    print "2. Manual Practice Mode"
    print "3. Quiz Mode"
    print "4. Return to Previous Menu"
    
    choice = raw_input("> ")
        
    if choice == ("1"):
        auto_practice()
    elif choice == ("2"):
        manual_practice()
    elif choice == ("3"):
        quiz()
    elif choice == ("4"):
        start()
    else:
        print "That is not an option. Please type 1, 2, 3, or 4."
        game()
    
    
def manual_practice():
    print "Enter the Game File You Wish to Play!"
    game_file = raw_input("> ")
    game_file_picklefied = (game_file + ".pickle")
    with open(game_file_picklefied, 'rb') as handle:
        word_set = pickle.load(handle)
        
    keys = word_set.keys()
    random.shuffle(keys)
    for key in keys:
        print ("\n" * 23), ("\t" * 4), key, '=', word_set[key], ("\n" * 23)
        raw_input("")
    game()

def auto_practice():
    print "Enter the Game File You Wish to Play!"
    game_file = raw_input("> ")
    game_file_picklefied = (game_file + ".pickle")
    with open(game_file_picklefied, 'rb') as handle:
        word_set = pickle.load(handle)
        
    print "Enter how many seconds you want each Word/Definition Set to appear on the screen."
    print "You can enter whole seconds or decimals such as 1.5 or .4"
    time_to_display = raw_input("> ")
    time_to_display_corrected = float(time_to_display)
    
    keys = word_set.keys()
    random.shuffle(keys)
    for key in keys:
        print ("\n" * 23), ("\t" * 4), key, '=', word_set[key], ("\n" * 23)
        time.sleep(time_to_display_corrected)
    game()
        
def quiz():
    print "Enter the Game File You Wish to Play!"
    game_file = raw_input("> ")
    game_file_picklefied = (game_file + ".pickle")
    with open(game_file_picklefied, 'rb') as handle:
        word_set = pickle.load(handle)
        
    keys = word_set.keys()
    random.shuffle(keys)
    for key in keys:
        print ("\n" * 23), ("\t" * 4), "Word: ", key, ("\n" * 23)
        print "Defintion: "
        answer = raw_input("> ")
        if answer == (word_set[key]):
            print ("\n" * 23), ("\t" * 4), 'Correct!', ("\n" * 23)
            time.sleep(1)
            pass
        else:
            print ("\n" * 23), ("\t" * 4), word_set[key], ("\n" * 23)
            time.sleep(1)
            pass
    game()

    
##########################################################################################

game_description()
