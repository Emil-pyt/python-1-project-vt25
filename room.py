
################################################
#This is a class that represents a room
#You can find the attributes of a room in the __init-method
################################################

from logging import debug
from random import randint, random

COLOR_NRM = "\033[0m"
COLOR_GREEN = "\033[1;32;40m"
COLOR_CYAN = "\033[1;36;40m" 
COLOR_WRN = "\033[1;93;40m"

class Room:
    num_instances = 0

    def __init__(self, name, room_id_s = -1, room_id_n = -1, room_id_e = -1, room_id_w = -1, room_txt = -1, item = -1, riddle = -1):
        self.id = type(self).num_instances #auto assign self.id
        type(self).num_instances += 1 #increment class attribute num_instances
        self.name = name
        self.room_id_s = room_id_s #id of room south of this room, key s
        self.room_id_n = room_id_n #id of room north of this room, key w
        self.room_id_e = room_id_e #id of room east of this room, key d
        self.room_id_w = room_id_w #id of room west of this room, key a
        self.room_txt = room_txt 
        self.item = item
        self.riddle = riddle
        self.item_list = []

    def add_into_item_list(self, item_name):
        self.item_list.append(item_name)

    def add_item_list(self, list_to_add):
        self.item_list.extend(list_to_add)

    def build_rand_err_msg(self):
        x = randint(1,7)
        ret_str = ""
        match x:
            case 1:
                ret_str = "The command does not exist, try again" 
            case 2:
                ret_str = "Oops wrong button, better luck next time"
            case 3: 
                ret_str = "Are you going to walk through a wall? Try a new button" 
            case 4: 
                ret_str =  "Great job pressing the wrong button. Try again"
            case 5: 
                ret_str =  "That doesn't seem right, maybe check which button you pressed"
            case 6:
                ret_str =  "You didn't read? Did you?"
            case 7:
                ret_str = "Oh snap! Wrong button"
        return ret_str

    # returns room id from usrinput_key: w, a, d, s
    def get_room_id(self, direction):
        return_value = -1
        match direction:
            case "a":
                return_value = self.room_id_w
            case "w":
                return_value = self.room_id_n
            case "d":
                return_value = self.room_id_e
            case "s":
                return_value = self.room_id_s
        return return_value
                
   

    def get_from_item_list(self, item_index):
        ret_val = ""
        if item_index < len(self.item_list):
            debug("popping index " + str(item_index) + " (" + self.item_list[item_index] + ")")
            ret_val = self.item_list.pop(item_index)
        else:
            ret_val = "Error: item_list index out of bound"
        return ret_val

    
    def generate_room_str(self, rooms_tuple, print_rand_msg, inv_p, required_list_p):        
        print_str = "You are now in the " + COLOR_CYAN + self.name + COLOR_NRM + "\n"  #name of room in bright green
        print_str = print_str + "\nThese are the items and order you need to collect to escape: " + str(required_list_p) + "\n"
        #print items in inventory list
        if len(inv_p) != 0:
            inv_str = ""
            color_str = ""
            for index, item in enumerate(inv_p):
                if item == required_list_p[index]:
                    color_str = COLOR_GREEN  #green
                else: 
                    color_str = COLOR_WRN
                inv_str = inv_str + color_str + str(item) + COLOR_NRM + ", "
            print_str = print_str + "Your inventory is: " + inv_str + "\n"

            #print which item are in this room
        if len(self.item_list) != 0:
            print_str = print_str + "These items can be picked up here by entering corresponding number: \n" 
            room_item_str = ""
            for index, item in enumerate(self.item_list):
                room_item_str = room_item_str + str(index) +". "+ str(item) + " "
            print_str = print_str + room_item_str + "\n"   
            #str = str + ', '.join(self.item_list) + "\n"
            

        print_str = print_str + "These are your options here: " + "\n"   
        if self.room_id_n != -1:
            print_str = print_str + (f"{' ': <30}{COLOR_GREEN + 'w' + COLOR_NRM +" -> " + rooms_tuple[self.room_id_n].name: <40}") + "\n" #prints the button cmds and highlights the key green
        if self.room_id_s != -1:
            print_str = print_str + (f"{' ': <30}{COLOR_GREEN + 's' + COLOR_NRM +" -> " + rooms_tuple[self.room_id_s].name: <40}") + "\n"
        if self.room_id_e != -1:
            print_str = print_str + (f"{' ': <30}{COLOR_GREEN + 'd' + COLOR_NRM +" -> " + rooms_tuple[self.room_id_e].name: <40}") + "\n"
        if self.room_id_w != -1:
            print_str = print_str + (f"{' ': <30}{COLOR_GREEN + 'a ' + COLOR_NRM + "-> " + rooms_tuple[self.room_id_w].name: <40}") + "\n"
        
        print_str = print_str + (f"{' ': <30}{COLOR_GREEN + 'z ' + COLOR_NRM + "-> back": <40}") + "\n"
        print_str = print_str + (f"{' ': <30}{COLOR_GREEN + 'i ' + COLOR_NRM + "-> inventory": <40}") + "\n"
        print_str = print_str + (f"{' ': <30}{COLOR_GREEN + 'p ' + COLOR_NRM + "-> break": <40}") + "\n"
        print_str = print_str + ("What do you want to do? \n")
        if print_rand_msg:
            print_str = print_str + self.build_rand_err_msg()
        return print_str
        