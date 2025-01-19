
#Todo: validate id and name
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

    def generate_input_str(self, rooms_tuple):

        str = "You are now in the " + "\033[1;36;40m" + self.name + "\033[0m" + "\n"  #name of room in bright green
        str = str + "These are your options here: " + "\n"
        if self.room_id_n != -1:
            str = str + (f"{' ': <30}{'w -> ' + rooms_tuple[self.room_id_n].name: <40}") + "\n"
        if self.room_id_s != -1:
            str = str + (f"{' ': <30}{'s -> ' + rooms_tuple[self.room_id_s].name: <40}") + "\n"
        if self.room_id_e != -1:
            str = str + (f"{' ': <30}{'d -> ' + rooms_tuple[self.room_id_e].name: <40}") + "\n"
        if self.room_id_w != -1:
            str = str + (f"{' ': <30}{'a -> ' + rooms_tuple[self.room_id_w].name: <40}") + "\n"
        
        str = str + (f"{' ': <30}{'z -> back ': <40}") + "\n"
        str = str + (f"{' ': <30}{'i -> inventory ': <40}") + "\n"
        str = str + (f"{' ': <30}{'p -> break': <40}") + "\n"
        str = str + ("Where do you want to go? ")
        return str