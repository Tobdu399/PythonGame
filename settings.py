# Modules to import:
from pynput.keyboard import Key, Listener
import pynput
import os
import random
import math

# Varibales:
GAME_CHARACTER = "+"
FOOD_CHARACTER = "#"
FOOD_AMOUNT = 3

CLEAR_COMMAND = "clear"
SCORE = 0
ROUND = 0

yellow = "\u001b[33m"
green = "\u001b[32m"
blue = "\u001b[36m"
red = "\u001b[31m"
white = "\u001b[37m"
black = "\u001b[30m"
reset = "\u001b[0m"

violet_bg = "\u001b[45m"
blue_bg = "\u001b[44m"
white_bg = "\u001b[47m"
black_bg = "\u001b[40m"
bold = "\u001b[1m"

bg_color = black_bg
border_color = blue
player_color = yellow
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
def clear():
    os.system(CLEAR_COMMAND)    

#! Don't change the code below this line
if __name__ == '__main__':
    exit()