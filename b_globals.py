#Board Markers
WATER = '?'
KILL = '#'
HIT = '!'
MISS = '-'

#Ships [length,marker]
CARRIER = 5
BATTLESHIP = 4
SUBMARINE = 3
DESTROYER = 3
CRUISER = 2

#Game Variables
players = ["dumb", "prob", "genetic", "farns"]
ships = [CARRIER, BATTLESHIP, SUBMARINE, DESTROYER, CRUISER]
ship_max_length = max(ships)
ship_min_length = min(ships)
board_size = 10
print_games = False
default = "dumb"
using_default = False
export_records = True
