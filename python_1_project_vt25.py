
from room import Room
from random import randint, random
import os
inventory = []

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

r0 = Room(name = "Pantry", room_id_n = 1)
r1 = Room(name = "Kitchen", room_id_n = 5, room_id_s = 0, room_id_e=2, room_id_w=3)
r1.add_into_item_list("Hammer")
r1.add_into_item_list("Broom")
r2 = Room(name = "Bedroom", room_id_n = 4, room_id_w = 1)
r2.add_into_item_list("Iron sword")
r3 = Room(name = "Main Living room", room_id_n = 6, room_id_w = 1)
r3.add_into_item_list("Rope")
r3.add_into_item_list("Paper")
r3.add_into_item_list("Pen")
r4 = Room(name = "Basement", room_id_s = 2)
r4.add_into_item_list("Iron")
r4.add_into_item_list("Iron")
r4.add_into_item_list("Iron")
r5 = Room(name = "Second Living room", room_id_e = 6, room_id_s = 1)
r6 = Room(name = "Hallway", room_id_w = 5, room_id_s = 3)
rooms = (r0, r1, r2, r3, r4, r5, r6)

current_room = rooms[0]
last_room = current_room

print_file('banner.txt')

print("Your goal is to collect material in the different rooms to fight the giant that is blocking the door so you can't escape. Good luck!")
print("To walk you use the commands:    W - South, A - East, D - West, S - back") 

print("Woah! You have just woken up. The room you're in is dark.")
print("You try to get out but the door is locked, try to find something in the room to smash the door.") 

while 1:   
    usrInput=input(current_room.generate_room_str(rooms))
    match usrInput:
        case "0"|"1"|"2"|"3":
            if int(usrInput) < len(current_room.item_list):  #if user pressed 0 make sure there are at least 1 item in the list
                inventory.append( current_room.get_from_item_list(int(usrInput)) )
            else:
                rand_Print()
        case "a":
            if current_room.room_id_w  != -1:
                last_room = current_room
            else: 
                rand_Print()
        case "w":
            if current_room.room_id_n  != -1:
                last_room = current_room
                current_room = rooms[current_room.room_id_n]
            else: 
                rand_Print()
        case "d":
            if current_room.room_id_e  != -1:
                last_room = current_room
                current_room = rooms[current_room.room_id_e]
            else: 
                rand_Print()
        case "s":
            if current_room.room_id_s  != -1:
                last_room = current_room
                current_room = rooms[current_room.room_id_s]
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
    print_file('banner.txt')


'''
    if room == 1:
        if lastRoom == 1:
            pantry()
        roomDialog(room, roomName = "Pantry", roomSouth = 2)
    if room == 2: 
        roomDialog(room, roomName = "livingroom", roomSouth = 6, roomWest = 3, roomEast = 4)
       
        #riddle in room 3
        print("You have found a paper behind the door. It seems like it's a riddle!? You take up the paper and read the riddle")
        print("The first digit is the number of weeks in two months.")
        print("The second digit is the number of months that have 28 days.")
        print("The third digit is the number of sides on a rectangle minus the number of sides on a triangle.")
        print("The fourth digit is the number of continents that start with the letter A.")
        print("What is the code? You could maybe need it in the future")
        '''

    # gor en lsita med inventory o titta om man kan skriva de under samma rad
    #todo 