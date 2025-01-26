
from room import Room
from random import randint, random
import os
import time

MAX_HP_CHARACTERS = 20 #number of printed stars when full hp
MAX_HP_SECONDS = 120 # seconds corresponding to MAX_HP_CHARACTERS
MAX_NR_SMOOTHIES = 4
HP_BOOSTER = "Health smoothie"
SMOOTHIE_EXTRA_SEC = 20

def print_file(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))


def rand_Print():
    x = randint(1,6)
    match x:
        case 1:
            str = "The command does not exist, try again" 
        case 2:
            str = "Oops wrong button, better luck next time"
        case 3: 
            str = "Are you going to walk through a wall? Try a new button" 
        case 4: 
            str =  "Great job pressing the wrong button. Try again"
        case 5: 
            str =  "That doesn't seem right, maybe check which button you pressed"
        case 6:
            str =  "You didn't read? Did you?"
        case 7:
            str = "Oh snap! Wrong button"
    print("\n-" + str + "\n") 
 
def calc_hp( nr_of_chars, nr_of_sec, start_time_p, smoothie_time_p):
    elapsed_time = time.perf_counter() - start_time_p - smoothie_time_p #might get negative but it´s okay if many smoothies taken early
    hp = round(nr_of_chars * (1-elapsed_time/nr_of_sec))
    return hp

def clear_screen():  
    if os.name == 'nt': 
        _ = os.system('cls')  # For Windows
    else:
        _ = os.system('clear') # For macOS and Linux


'''
initialization
creates room objects and add them to the "rooms" tuple
also adds item to the rooms
'''
nr_smoothies = MAX_NR_SMOOTHIES
r0 = Room(name = "Pantry", room_id_n = 1)
r0.add_item_list(["Canned jars", "Bread"])
r1 = Room(name = "Kitchen", room_id_n = 5, room_id_s = 0, room_id_e=2, room_id_w=3)
r1.add_item_list([HP_BOOSTER, "Broom"])

r2 = Room(name = "Bedroom", room_id_n = 4, room_id_w = 1)
r2.add_into_item_list("Iron sword")

r3 = Room(name = "Main Living room", room_id_n = 6, room_id_w = 1)
r3.add_item_list(["Paper", "Pen", "Rope"])

r4 = Room(name = "Basement", room_id_s = 2)
r4.add_item_list(["Alarm code", "Torch", "Key"])

r5 = Room(name = "Second Living room", room_id_e = 6, room_id_s = 1)
r5.add_item_list(["Hammer"])

r6 = Room(name = "Hallway", room_id_w = 5, room_id_s = 3, room_id_n = 7)
r7 = Room(name = "Garden")
rooms_in_house = (r0, r1, r2, r3, r4, r5, r6, r7)
smoothie_time = 0
current_room = rooms_in_house[0] #holds which object in the tuple that is in focus
last_room = current_room #to be able to go back
inventory = []
print_file('banner_zork.txt')

print("Your goal is to collect material in the different rooms to fight the giant that is blocking the door so you can't escape. Good luck!")
print("To walk you use the commands:    W - South, A - East, D - West, S - back") 

print("Woah! You have just woken up. The room you're in is dark.")
print("You try to get out but the door is locked, try to find something in the room to smash the door.") 

start_time = time.perf_counter()
while 1:
    usrInput=input(current_room.generate_room_str(rooms_in_house))

    match usrInput:
        case "0"|"1"|"2"|"3":
            if int(usrInput) < len(current_room.item_list):  #if user pressed 0 make sure there are at least 1 item in the list
                inventory.append( current_room.get_from_item_list(int(usrInput)) )
                if HP_BOOSTER in inventory: #if we added HP_BOOSTER in inventory -> pop it and add extra seconds to hp calc
                    inventory.pop( inventory.index( HP_BOOSTER ) ) 
                    smoothie_time += SMOOTHIE_EXTRA_SEC
            else:
                rand_Print()
        case "a"|"d"|"w"|"s":
            new_room_id = current_room.get_room_id(usrInput)
            if new_room_id  != -1:
                last_room = current_room
                current_room = rooms_in_house[new_room_id]
            else: 
                rand_Print()

        case "z": # going back
            (current_room, last_room) = (last_room, current_room) #instead of using a tmp variable
        case "i":
            print (inventory)
        case "p":
            exit()
        case _:
            rand_Print()
    clear_screen()
    
    hp = calc_hp(MAX_HP_CHARACTERS, MAX_HP_SECONDS, start_time, smoothie_time)
    if hp >= 0:
        print_file('banner_zork.txt')
        print("Your health is:  " + "*" * hp + "-" * (20-(hp)))
    else:
        print_file('banner_game_over.txt')
        print("You have died...")
        exit()
        
        #when leaving kitchen check if we should add a new health smoothie
    if last_room.id == 1 and nr_smoothies > 0 and r1.item_list.count(HP_BOOSTER) == 0:
        r1.add_into_item_list(HP_BOOSTER)
        nr_smoothies -= 1
        
        
'''
   
        #riddle in room 3
        print("You have found a paper behind the door. It seems like it's a riddle!? You take up the paper and read the riddle")
        print("The first digit is the number of weeks in two months.")
        print("The second digit is the number of months that have 28 days.")
        print("The third digit is the number of sides on a rectangle minus the number of sides on a triangle.")
        print("The fourth digit is the number of continents that start with the letter A.")
        print("What is the code? You could maybe need it in the future")
        '''
