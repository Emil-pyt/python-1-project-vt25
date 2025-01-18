

from email.policy import default


Hp = 5
#Nycklar = 0
#Hammare = 0
room=1
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


def rum_1():
    print("Valkommen, du ar i rum_1 ") 
def rum_2():
    print("Valkommen, du ar i rum_2 ")




 
print("Welcome! You are stuck in a abondend house. Your goal is to collect material in the different rooms to fight the giant that is blocking the door so you can't escape. Good luck!")
print("To walk you use the commands:    W - Forward, A - left, D - right, S - backwards")
while 1:
    if room == 1:
        rum_1()
        usrInput=input("Where do you want to go? (forward) ")
        match usrInput:
            case "w":
                lastRoom = room
                room = 2
            case _:
                print("The command does not exist, try again ")
    if room == 2: 
        rum_2()
        usrInput=input("Where do you want to go? (Left, right, forward, back) ")
        match usrInput:
            case "a":
                lastRoom = room
                room = 4
            case "w":
                lastRoom = room
                room = 6
            case "d":
                lastRoom = room
                room = 3
            case "s": # going back
                tmp_room = room #save current room in tmp variable
                room = lastRoom 
                lastRoom = tmp_room
            case "i":
                print(Inventory)
            case _:
                print("The command does not exist, try again ")
    if room == 3: 
         print("You are in room 3")
         print("You have found a paper behind the door. It seems like it's a riddle!? You take up the paper and read the riddle")
         print("The first digit is the number of weeks in two months.")
         print("The second digit is the number of months that have 28 days.")
         print("The third digit is the number of sides on a rectangle minus the number of sides on a triangle.")
         print("The fourth digit is the number of continents that start with the letter A.")
         print("What is the code? You could maybe need it in the future")

         usrInput=input("Where do you want to go? (left or back) ")
         match usrInput:
             case "a":
                 lastRoom = room
                 room = 5
             case "s": # going back
                tmp_room = room #save current room in tmp variable
                room = lastRoom 
                lastRoom = tmp_room
             case "i":
                print(Inventory)
             case _:
                print("The command does not exist, try again ")
    if room == 4:
        print("You are in room 4")
        usrInput=input("Where do you want to go? (right or back) ")
        match usrInput: 
            case "d":
                lastRoom = room
                room = 7
            case "s": # going back
                tmp_room = room #save current room in tmp variable
                room = lastRoom 
                lastRoom = tmp_room
            case "i":
                print(Inventory)
            case _:
                print("The command does not exist, try again ")
    if room == 5:
        print("You are in room 5") # the basement
        usrInput=input("Where do you want to go? (back) ")
        match usrInput: 
            case "s": # going back
                tmp_room = room #save current room in tmp variable
                room = lastRoom 
                lastRoom = tmp_room
            case _:
                print("The command does not exist, try again ")
    if room == 6:
        print("You are in room 6")
        usrInput=input("Where do you want to go? (left or back) ")
        match usrInput: 
            case "a":
                lastRoom = room
                room = 7
            case "s": # going back
                tmp_room = room #save current room in tmp variable
                room = lastRoom 
                lastRoom = tmp_room
            case "i":
                print(Inventory)
            case _:
                print("The command does not exist, try again ")
    if room == 7:
        print("You are in room 7, the final room")
        usrInput=input("Where do you want to go? ( or back) ")
        match usrInput: 
            case "d":
                lastRoom = room
                room = 7
            case "s": # going back
                tmp_room = room #save current room in tmp variable
                room = lastRoom 
                lastRoom = tmp_room
            case "i":
                print(Inventory)
            case _:
                print("The command does not exist, try again ")
                