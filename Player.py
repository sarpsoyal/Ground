#Move these somewhere else please
#A list that holds all room objects
rooms = []

#Returns the room with the given name
def GetRoom(roomName):
    for room in rooms:
        if room.name == roomName:
            return room
#Returns the room that player currently is in
def CurrentRoom():
    for room in rooms:
        if room.active:
            return room

class Player:

    #Players inventory
    inventory = []

    #Constructor function, sets the name of the player
    def __init__(self, name):
        self.name = name

    #Main logic engine
    def Logic(self, usrInp):
        #Split the sentence into a list of words
        words = usrInp.split()

        #Procedure for one word inputs
        if len(words) == 1:
            #User wants to go north
            if words[0].lower() == 'north' or words[0].lower() == 'n':
                return CurrentRoom().North()
            #User wants to go south
            elif words[0].lower() == 'south' or words[0].lower() == 's':
                return CurrentRoom().South()
            #User wants to go west
            elif words[0].lower() == 'west' or words[0].lower() == 'w':
                return CurrentRoom().West()
            #User wants to go east
            elif words[0].lower() == 'east' or words[0].lower() == 'e':
                return CurrentRoom().South()
            #User wants to go up
            elif words[0].lower() == 'up' or words[0].lower() == 'u':
                return CurrentRoom().Up()
            #User wants to go down
            elif words[0].lower() == 'down' or words[0].lower() == 'd':
                return CurrentRoom().Down()
            #User needs help with commands
            elif words[0].lower() == 'help':
                return self.Help()
            #User wants to look around
            elif words[0].lower() == 'look':
                return CurrentRoom().Look()
            #Unknown Input
            else:
                return 'Unrecognized input, use -help-'

        #Procedure for two word inputs
        elif len(words) == 2:
            return 'Error, two word inputs not yet implemented!'
        #Procedure for inputs with more than two words
        elif len(words) > 2:
            return 'Error, more than two word inputs not yet implemented!'
        #If there is no input
        else:
            return 'Error, no input recieved!'

    #Runs when user uses help command, returns emergency ambulance
    def Help(self):
        return 'Daa Deeee Daaa Deee'
