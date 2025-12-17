import os


WALL = '#'
WAY = ' '
PLAYER = '+'
EXIT = '$'
VISITED = '·'
MAX_LEVELS = 5

def clear_consol():
    os.system('cls' if os.name == 'nt' else 'clear')
