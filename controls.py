import settings as gs
if __name__ == '__main__':
    print(gs.wrong_file_msg + __file__)
    exit()
# Don't change the code above this line

from game import game

def on_press(key):
    if key == gs.Key.right and game.x_pos < game.map_width-2:
        game.player_dir(1, 0)
    if key == gs.Key.left and game.x_pos > 1:
        game.player_dir(-1, 0)
    if key == gs.Key.down and game.y_pos < game.map_height-2:
        game.player_dir(0, 1)
    if key == gs.Key.up and game.y_pos > 1:
        game.player_dir(0, -1)

    else:
        game.player_dir(0, 0)

def on_release(key):
    if key == gs.Key.esc:
        gs.clear()
        return False