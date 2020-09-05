if __name__ == '__main__':
    exit()
#? ^ Had to move that piece of code from the bottom of this file up here
#?   due to an import error which occures when the user tries to run this file

import settings as gs
from player import player

def on_press(key):
    if key == gs.Key.right and player.x_pos < player.map_width-2:
        player.move(1, 0)
        player.direction = "right"
    if key == gs.Key.left and player.x_pos > 1:
        player.move(-1, 0)
        player.direction = "left"
    if key == gs.Key.down and player.y_pos < player.map_height-2:
        player.move(0, 1)
        player.direction = "down"
    if key == gs.Key.up and player.y_pos > 1:
        player.move(0, -1)
        player.direction = "up"

    else:
        player.move(0, 0)

def on_release(key):
    if key == gs.Key.esc:
        gs.end_game()