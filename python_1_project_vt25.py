
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


def roomDialog(parRoom, roomName, roomSouth = 0, roomWest = 0, roomEast = 0):
    if roomName != pantry:
        print("You are now in the " + roomName)  
    print("These are your options here: ")
    if roomSouth != 0:
       print(f"{'South (w)': >42}")
    if roomEast != 0:
       print(f"{'East (a)': >42}")
    if roomWest != 0:
        print(f"{'West (d)': >42}")
    if roomName != "room 1":
        print(f"{'back (s)': >42}")
    print(f"{'inventory (i)': >42}")
    global room
    global lastRoom
    usrInput=input("Where do you want to go? ")
    match usrInput:
        case "a":
            if roomEast != 0:
                lastRoom = parRoom
                room = roomEast
            else: 
                print("You didn't reed? Did you?")
        case "w":
            if roomSouth != 0:
                lastRoom = parRoom
                room = roomSouth
            else: 
                print("You didn't reed? Did you?")
        case "d":
            if roomWest != 0:
                lastRoom = parRoom
                room = roomWest
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
def intro():
    print("Your goal is to collect material in the different rooms to fight the giant that is blocking the door so you can't escape. Good luck!")
    print("To walk you use the commands:    W - South, A - East, D - West, S - back") 
def pantry():
    print("Woah! You have just woken up. The room you're in is dark.")
    print("You try to get out but the door is locked, so you feel around in the room trying to find something heavy to smash the door.") 
    print("You are lucky this time, the room seems to have a lot of food and kitchen ware so you can quickly find a mortal to smash the door") 






  
intro()
while 1:
    if room == 1:
        if lastRoom == 1:
            pantry()
        roomDialog(room, roomName = "Pantry", roomSouth = 2)
    if room == 2: 
        roomDialog(room, roomName = "livingroom", roomSouth = 6, roomWest = 3, roomEast = 4)
       
    if room == 3: 
        print("You are in room 3")
        print("You have found a paper behind the door. It seems like it's a riddle!? You take up the paper and read the riddle")
        print("The first digit is the number of weeks in two months.")
        print("The second digit is the number of months that have 28 days.")
        print("The third digit is the number of sides on a rectangle minus the number of sides on a triangle.")
        print("The fourth digit is the number of continents that start with the letter A.")
        print("What is the code? You could maybe need it in the future")
        roomDialog(room, roomName = "3, the livingroom", roomEast = 5) 
    if room == 4:
        roomDialog(room, roomName = "4", roomSouth = 7, roomWest = 2)
    if room == 5:
        roomDialog(room, roomName = "5, basement")
    if room == 6:
        roomDialog(room, roomName = "the kitchen", roomEast = 7)      
    if room == 7:
        roomDialog(room, roomName = "7, the final room", roomWest = 7)

        #rum 4
        # dop om till riktningar - vaderstrack
        #rand for om man skriver fel
        # fy den att inte printa pantry f rsta g ngen n r def k rs
        # rum 2  r k k, rum 3 sovrum, rum 5 k llare, 