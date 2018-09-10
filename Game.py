from Player import *
from Room import *
from Item import *

#Setup basic testing environment
player = Player('Sarp')
lobby = Room('lobby', 'A long empty room covered with a red carpet. There is a large door on the north side of the room.', rooms)
waitingRoom = Room('waitingRoom', 'You find yourself in a square room with a round table and lots of chairs. There is a door on the south side of the room', rooms)
mainDoor = Way('lobby', 'waitingRoom', 'North', 'South')
key = Item('key', 'You see a shiny golden key on the floor.', 'OPENS_KITCHEN', 0.1)
key.Add(waitingRoom)

#Put player into starting room
lobby.active = True

#Run the game loop
while True:
    print(player.Logic(raw_input()))
