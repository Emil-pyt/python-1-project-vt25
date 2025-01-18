
#Todo: validate id and name
class Room:
    def __init__(self, id, name, nxt_south = -1, nxt_north = -1, nxt_east = -1, nxt_west = -1, room_txt = -1, item = -1, riddle = -1):
        self.id = id
        self.name = name
        self.nxt_south = nxt_south
        self.nxt_north = nxt_north
        self.nxt_east = nxt_east
        self.nxt_west = nxt_east
        self.nxt_west = nxt_east
        self.room_txt = room_txt
        self.item = item
        self.riddle = riddle

    def dialog(self):
        print("You are now in the " + self.name)
        print("These are your options here: ")
        if self.nxt_south != -1:
           print(f"{'South (s)': >42}")
        if self.nxt_north != -1:
           print(f"{'North (w)': >42}")
        if self.nxt_east != -1:
           print(f"{'East (d)': >42}")
        if self.nxt_west != -1:
            print(f"{'West (a)': >42}")
        if self.id != -1:
            print(f"{'back (z)': >42}")
        print(f"{'inventory (i)': >42}")
        print("Where do you want to go? ")
        


        