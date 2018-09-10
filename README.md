# Ground

Ground is an very easy and lightweight library to create your next python text-based game.

## Features

### Character/Inventory
  Easily initiate the player and its inventory
  ```python
  player1 = Player('playerName')
  ```
### Zone Control
  Create any number of zones/rooms with up to 6 connections to any other created zone just using a single line of code.
  ```python
  lobby = Room('lobby', 'A long empty room covered with a red carpet. There is a large door on the north side of the room.', rooms) # zoneName, zoneDescription, containerList
  mainDoor = Way('lobby', 'kitchen', 'North', 'South') # zone1, zone2, zone1Position, zone2Position
  ```
### Items Management
  Create and add items to your world
  ```python
  key = Item('key', 'You see a shiny golden key on the floor.', 'OPENS_KITCHEN', 0.1) # itemName, itemDescription, itemFunction, itemWeight
  key.Add(waitingRoom) # roomToContainItem
  ```
### Player Controls
  Very simple yet effective commands for in-game player control
  ```python
  look # Describes the current environment and visible items to the player
  take 'itemName' # Attempts to add an item to the players inventory
  north # Moves the player towards the given direction

