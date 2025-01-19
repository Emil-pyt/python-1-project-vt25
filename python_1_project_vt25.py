
from room import Room


inventory = []

def print_file(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))

 
r0 = Room(name = "Pantry", room_id_n = 1)
r1 = Room(name = "Kitchen", room_id_n = 5, room_id_s = 0, room_id_e=2, room_id_w=3)
r2 = Room(name = "Bedroom", room_id_n = 4, room_id_w = 1)
r3 = Room(name = "Main Living room", room_id_n = 6, room_id_w = 1)
r4 = Room(name = "Basement", room_id_s = 2)
r5 = Room(name = "Second Living room", room_id_e = 6, room_id_s = 1)
r6 = Room(name = "Hallway", room_id_w = 5, room_id_s = 3)
rooms = (r0, r1, r2, r3, r4, r5, r6)

current_room = rooms[0]
last_room = current_room

print_file('banner.txt')


print("Your goal is to collect material in the different rooms to fight the giant that is blocking the door so you can't escape. Good luck!")
print("To walk you use the commands:    W - South, A - East, D - West, S - back") 

print("Woah! You have just woken up. The room you're in is dark.")
print("You try to get out but the door is locked, so you feel around in the room trying to find something heavy to smash the door.") 
print("You are lucky this time, the room seems to have a lot of food and kitchen ware so you can quickly find a mortal to smash the door") 


while 1:   
    usrInput=input(current_room.generate_input_str(rooms))
    match usrInput:
        case "a":
            if current_room.room_id_w  != -1:
                last_room = current_room
                current_room = rooms[current_room.room_id_w]
            else: 
                print("You didn't read? Did you?")
        case "w":
            if current_room.room_id_n  != -1:
                last_room = current_room
                current_room = rooms[current_room.room_id_n]
            else: 
                print("You didn't read? Did you?")
        case "d":
            if current_room.room_id_e  != -1:
                last_room = current_room
                current_room = rooms[current_room.room_id_e]
            else: 
                print("You didn't read? Did you?")
        case "s":
            if current_room.room_id_s  != -1:
                last_room = current_room
                current_room = rooms[current_room.room_id_s]
            else: 
                print("You didn't read? Did you?")
        case "z": # going back
            tmp_room = current_room #save current room in tmp variable
            current_room = last_room 
            last_room = current_room
        case "i":
            print(Inventory)
        case "p":
            exit()
        case _:
            print("The command does not exist, try again ")



'''
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
        '''