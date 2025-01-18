
from email.policy import default


Hp = 5
room = 1
lastRoom = 1
Svard = 0
Inventory = []

#def when_clicked("e"):
#    print(Inventory)

#import keyboard
#    while True:
#       if keyboard.read_key() == "p":
#            print("You pressed p")
#import tkinter as tk


def roomDialog(parRoom, roomName, roomFwd = 0, roomRight = 0, roomLeft = 0):
    print("You are now in room " + roomName)  
    print("These are your options here: ")
    if roomFwd != 0:
       print(f"{'forward (w)': >42}")
    if roomLeft != 0:
       print(f"{'left (a)': >42}")
    if roomRight != 0:
        print(f"{'right (d)': >42}")
    if roomName != "room 1":
        print(f"{'back (s)': >42}")
    print(f"{'inventory (i)': >42}")
    global room
    global lastRoom
    usrInput=input("Where do you want to go? ")
    match usrInput:
        case "a":
            if roomLeft != 0:
                lastRoom = parRoom
                room = roomLeft
            else: 
                print("You didn't reed? Did you?")
        case "w":
            if roomFwd != 0:
                lastRoom = parRoom
                room = roomFwd
            else: 
                print("You didn't reed? Did you?")
        case "d":
            if roomRight != 0:
                lastRoom = parRoom
                room = roomRight
            else: 
                print("You didn't reed? Did you?")
        case "s": # going back
            tmp_room = parRoom #save current room in tmp variable
            room = lastRoom 
            lastRoom = tmp_room
        case "i":
            print(Inventory)
        case _:
            print("The command does not exist, try again ")
    return







 
print("Welcome! You are stuck in a abondend house. Your goal is to collect material in the different rooms to fight the giant that is blocking the door so you can't escape. Good luck!")
print("To walk you use the commands:    W - Forward, A - left, D - right, S - backwards")
while 1:
    if room == 1:
        roomDialog(room, roomName = "room 1", roomFwd = 2)
    if room == 2: 
        roomDialog(room, roomName = "Kitchen", roomFwd = 6, roomRight = 3, roomLeft = 4)
       
    if room == 3: 
        print("You are in room 3")
        print("You have found a paper behind the door. It seems like it's a riddle!? You take up the paper and read the riddle")
        print("The first digit is the number of weeks in two months.")
        print("The second digit is the number of months that have 28 days.")
        print("The third digit is the number of sides on a rectangle minus the number of sides on a triangle.")
        print("The fourth digit is the number of continents that start with the letter A.")
        print("What is the code? You could maybe need it in the future")
        roomDialog(room, roomName = "3, the livingroom", roomLeft = 5) 
    if room == 4:
        roomDialog(room, roomName = "4", roomRight = 7)
    if room == 5:
        roomDialog(room, roomName = "5, the basement")
    if room == 6:
        roomDialog(room, roomName = "6", roomLeft = 7)      
    if room == 7:
        roomDialog(room, roomName = "7, the final room", roomRight = 7)

        #rum 4
        # d p om till riktningar - v derstr ck
