# Modules to import:
from pynput.keyboard import Key, Listener
import os
import random
import math
import threading
import time

# Varibales:
PLAYER_CHARACTER = "+"
FOOD_CHARACTER = "#"
FOOD_AMOUNT = 3
ENEMY_AMOUNT = 3
SCORE = 0
ROUND = 0

GAME = True

yellow = "\u001b[33m"
green = "\u001b[32m"
blue = "\u001b[36m"
magenta = "\u001b[35m"
red = "\u001b[31m"
black = "\u001b[30m"
reset = "\u001b[0m"

violet_bg = "\u001b[45m"
black_bg = "\u001b[40m"
bold = "\u001b[1m"

bg_color = black_bg
border_color = blue
player_color = yellow
enemy_color = magenta
food_color = red

# Gameboard
gameboard = ["/----------------------------\\",
            "|                            |",
            "|                            |",
            "|                            |",
            "|                            |",
            "|                            |",
            "|                            |",
            "|                            |",
            "|                            |",
            "\\----------------------------/",
            ]

# Functions
clear = lambda: os.system("clear" if os.name!='nt' else "cls")

#! Don't change the code below this line
if __name__ == '__main__':
    exit()