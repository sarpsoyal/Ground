class Item:

    #Constructor function, sets the name, description, usage and the size of the item
    def __init__(self, name, description, usage, size):
        self.name = name
        self.description = description
        self.usage = usage
        self.size = size

    #Add function, adds the item to the spesified room
    def Add(self, room):
        room.items.append(self)
