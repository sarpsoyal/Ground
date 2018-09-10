from Player import *
class Room:

    #Is set true if player is currently in this room
    active = False
    #Is set true if player has ever visited this room
    visited = False
    #List that contains all ways connected to this room
    ways = []
    #Items currently present in this room
    items = []

    #Constructor function, sets the name and the description of the room
    def __init__(self, name, description, rooms):
        self.name = name
        self.description = description
        rooms.append(self)

    #Visit function, runs when player enters this room by a connected way. Returns the description of the room if it is being visited for the first time
    def Visit(self):
        self.active = True
        if not self.visited:
            return self.description
        else:
            self.visited = True
            return ''

    #Look function, returns a string that briefly describes the current room by printing the description of the room and the contained ways and items
    def Look(self):
        result = self.description
        for item in self.items:
            result = result + ' ' + item.description
        return result

    #North function, travels using the way if there is one on the north of the room, else returns an error
    def North(self):
        for way in self.ways:
            if way.fromRoom == self.name and way.fromDir == 'North':
                return way.Travel(self.name)
            elif way.toRoom == self.name and way.toDir == 'North':
                return way.Travel(self.name)
            else:
                return 'You can not go there, there is a wall.'

    #South function, travels using the way if there is one on the south of the room, else returns an error
    def South(self):
        for way in self.ways:
            if way.fromRoom == self.name and way.fromDir == 'South':
                way.Travel(self.name)
                return ''
            elif way.toRoom == self.name and toDir == 'South':
                way.Travel(self.name)
                return ''
            else:
                return 'You can not go there, there is a wall.'

    #West function, travels using the way if there is one on the west of the room, else returns an error
    def West(self):
        for way in self.ways:
            if way.fromRoom == self.name and fromDir == 'West':
                way.Travel(self.name)
                return ''
            elif way.toRoom == self.name and toDir == 'West':
                way.Travel(self.name)
                return ''
            else:
                return 'You can not go there, there is a wall.'

    #East function, travels using the way if there is one on the east of the room, else returns an error
    def East(self):
        for way in self.ways:
            if way.fromRoom == self.name and fromDir == 'East':
                way.Travel(self.name)
                return ''
            elif way.toRoom == self.name and toDir == 'East':
                way.Travel(self.name)
                return ''
            else:
                return 'You can not go there, there is a wall.'

    #Up function, travels using the way if there is one upwards of the room, else returns an error
    def Up(self):
        for way in self.ways:
            if way.fromRoom == self.name and fromDir == 'Up':
                way.Travel(self.name)
                return ''
            elif way.toRoom == self.name and toDir == 'Up':
                way.Travel(self.name)
                return ''
            else:
                return 'There is no way up.'

    #Down function, travels using the way if there is one downwards of the room, else returns an error
    def Down(self):
        for way in self.ways:
            if way.fromRoom == self.name and fromDir == 'Down':
                way.Travel(self.name)
                return ''
            elif way.toRoom == self.name and toDir == 'Down':
                way.Travel(self.name)
                return ''
            else:
                return 'There is no way down'

class Way:

    #Constructor function, sets the connected rooms and the directions connected from
    def __init__(self, fromRoom, toRoom, fromDir, toDir):
        global GetRoom
        self.fromRoom = fromRoom
        self.toRoom = toRoom
        self.fromDir = fromDir
        self.toDir = toDir
        GetRoom(fromRoom).ways.append(self)
        GetRoom(toRoom).ways.append(self)

    #Travel function, takes the room to travel from as a parameter and runs the visit function of the connected room.
    def Travel(self, whereFrom):
        if whereFrom == self.fromRoom:
            GetRoom(self.fromRoom).active = False
            return GetRoom(self.toRoom).Visit()
        elif whereFrom == self.toRoom:
            GetRoom(self.toRoom).active = False
            return GetRoom(self.fromRoom).Visit()
