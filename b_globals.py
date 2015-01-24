#Board Markers
WATER = 'W'
KILL = 'K'
HIT = 'H'
MISS = 'M'

#Ships [length,marker]
CARRIER = 5
BATTLESHIP = 4
SUBMARINE = 3
DESTROYER = 3
CRUISER = 2

#Game Variables
ships = [CARRIER, BATTLESHIP, SUBMARINE, DESTROYER, CRUISER]
ship_max_length = max(ships)
ship_min_length = min(ships)
default = "dumb"
board_size = 10
print_games = True
