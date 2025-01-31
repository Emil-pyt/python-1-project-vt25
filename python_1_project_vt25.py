################################################
# Main function that creates objects from the room class
# and then let the player go to different rooms.
################################################

from room import Room
import os
import time
from random import randint, random

#Settings
MAX_HP_CHARACTERS = 20 #number of printed stars when full hp
MAX_HP_SECONDS = 120 # seconds corresponding to MAX_HP_CHARACTERS
MAX_NR_SMOOTHIES = 4
HP_BOOSTER = "Health smoothie"
SMOOTHIE_EXTRA_SEC = 20
REQUIRED_LIST = ["Alarm code", "Bread", "Torch"]

# print banner file
def print_file(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))



# calculate hp from elapsed time and nr of taken smoothies
def calc_hp( nr_of_chars, nr_of_sec, start_time_p, smoothie_time_p):
    elapsed_time = time.perf_counter() - start_time_p - smoothie_time_p #might get negative but it´s okay if many smoothies taken early
    hp = round(nr_of_chars * (1-elapsed_time/nr_of_sec))
    return hp

# clears the screen 
def clear_screen():  
    if os.name == 'nt': 
        _ = os.system('cls')  # For Windows
    else:
        _ = os.system('clear') # For macOS and Linux



#initialization
#creates room objects and add them to the "rooms" tuple
#also adds item to the rooms

nr_smoothies = MAX_NR_SMOOTHIES
r0 = Room(name = "Pantry", room_id_n = 1)
r0.add_item_list(["Canned jars", "Bread"])
r1 = Room(name = "Kitchen", room_id_n = 5, room_id_s = 0, room_id_e=2, room_id_w=3)
r1.add_item_list( [HP_BOOSTER, "Broom"] )

r2 = Room(name = "Bedroom", room_id_n = 4, room_id_w = 1)
r2.add_into_item_list("Ipad")

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

print("Your goal is to collect material in the different rooms to escape the house you are locked inside. Good luck!")
print("To walk you use the commands:    W - North, A - West, D - East, S - South") 

start_time = time.perf_counter()
print_err_msg = False
while 1:
    usrInput=input(current_room.generate_room_str(rooms_in_house, print_err_msg, inventory, REQUIRED_LIST))
    print_err_msg = False
    match usrInput:
        case "0"|"1"|"2"|"3": #pick an item into inventory-list
            if int(usrInput) < len(current_room.item_list):  #if user pressed 0 make sure there are at least 1 item in the list
                inventory.append( current_room.get_from_item_list(int(usrInput)) )
                if HP_BOOSTER in inventory: #if we added HP_BOOSTER in inventory -> pop it and add extra seconds to hp calc
                    inventory.pop( inventory.index( HP_BOOSTER ) ) 
                    smoothie_time += SMOOTHIE_EXTRA_SEC
            else:
                print_err_msg = True
        case "a"|"d"|"w"|"s": #enter neighbouring room
            new_room_id = current_room.get_room_id(usrInput)
            if new_room_id  != -1:
                last_room = current_room
                current_room = rooms_in_house[new_room_id]
            else: 
                print_err_msg = True
        case "z": # going back
            (current_room, last_room) = (last_room, current_room) #instead of using a tmp variable
        case "p":
            exit()
        case _:
            print_err_msg = True 
    clear_screen() 
    
    
    hp = calc_hp(MAX_HP_CHARACTERS, MAX_HP_SECONDS, start_time, smoothie_time)
    # check if game over
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
        #when going into garden room check if we have the correct inventory to win the game otherwise go back to last room and flush inventory
    if current_room == rooms_in_house[-1]: 
        if inventory == REQUIRED_LIST:
                clear_screen()
                print_file('banner_won.txt')
                exit()
        else:
            print("\033[1;93;40m" + "Not correct items in inventory. You have lost all your inventories and you were pushed back into " + rooms_in_house[-2].name  + "\033[0m" + "\n")
            #put requierd items into rooms so the usr gets a second chance
            for item in inventory:
                room_rand_number = randint(0, len(rooms_in_house)-2) #-2 since we dont want to place items in last room(garden)
                rooms_in_house[room_rand_number].add_into_item_list(item)  
            inventory = []
            current_room = last_room #forces the usr back into the house
