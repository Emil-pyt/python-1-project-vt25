
#Todo: validate id and name
# comment methods and functions
class Room:
    num_instances = 0

    def __init__(self, name, room_id_s = -1, room_id_n = -1, room_id_e = -1, room_id_w = -1, room_txt = -1, item = -1, riddle = -1):
        self.id = type(self).num_instances #auto assign self.id
        type(self).num_instances += 1 #increment class attribute num_instances
        self.name = name
        self.room_id_s = room_id_s #id of room south of this room
        self.room_id_n = room_id_n #id of room north of this room
        self.room_id_e = room_id_e #id of room east of this room
        self.room_id_w = room_id_w #id of room west of this room
        self.room_txt = room_txt 
        self.item = item
        self.riddle = riddle
        self.item_list = []

    def add_item_list(self, item_name):
        self.item_list.append(item_name)
        
        
    
    def generate_input_str(self, rooms_tuple):

        print_str = "You are now in the " + "\033[1;36;40m" + self.name + "\033[0m" + "\n"  #name of room in bright green
        if len(self.item_list) != 0:
            print_str = print_str + "Press a number of wich item you want to pick up: \n" #print all items if any            
            item_str = ""
            for index, item in enumerate(self.item_list):
                item_str = item_str + str(index) +". "+ str(item) + " "
            print_str = print_str + item_str + "\n"   
            #str = str + ', '.join(self.item_list) + "\n"
        print_str = print_str + "These are your options here: " + "\n"   
        if self.room_id_n != -1:
            print_str = print_str + (f"{' ': <30}{"\033[1;32;40m" + 'w' "\033[0m" +" -> " + rooms_tuple[self.room_id_n].name: <40}") + "\n" #prints the button cmds and highlights the key green
        if self.room_id_s != -1:
            print_str = print_str + (f"{' ': <30}{"\033[1;32;40m" + 's' "\033[0m" +" -> " + rooms_tuple[self.room_id_s].name: <40}") + "\n"
        if self.room_id_e != -1:
            print_str = print_str + (f"{' ': <30}{"\033[1;32;40m" + 'd' "\033[0m" +" -> " + rooms_tuple[self.room_id_e].name: <40}") + "\n"
        if self.room_id_w != -1:
            print_str = print_str + (f"{' ': <30}{"\033[1;32;40m" + 'a ' "\033[0m" + "-> " + rooms_tuple[self.room_id_w].name: <40}") + "\n"
        
        print_str = print_str + (f"{' ': <30}{"\033[1;32;40m" + 'z ' "\033[0m" + "-> back": <40}") + "\n"
        print_str = print_str + (f"{' ': <30}{"\033[1;32;40m" + 'i ' "\033[0m" + "-> inventory": <40}") + "\n"
        print_str = print_str + (f"{' ': <30}{"\033[1;32;40m" + 'p ' "\033[0m" + "-> break": <40}") + "\n"
        print_str = print_str + ("Where do you want to go? ")
        return print_str