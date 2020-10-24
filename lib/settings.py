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
ENEMY_CHARACTER = ("C", "Ɔ")
FOOD_AMOUNT = 5
ENEMY_AMOUNT = 4
SCORE = 0
ROUND = 0

GAME = True
TIME = 0
REFRESH_RATE = 0.5
SPAWNING_RATE = 1.5

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
enemy_spawn_color = yellow

# Gameboard
gameboard = ["/--------------------------------\\",
            "|                                |",
            "|                                |",
            "|                                |",
            "|                                |",
            "|                                |",
            "|                                |",
            "|                                |",
            "|                                |",
            "\\--------------------------------/",
            ]

# Functions
clear = lambda: os.system("clear" if os.name != 'nt' else "cls")

def end_game():
    global GAME
    GAME = False
    clear()
    exit()

if __name__ == '__main__':
    exit()
