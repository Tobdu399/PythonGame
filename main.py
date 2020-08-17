import sourcedefender
import settings as gs
import controls
import obstacle
from game import game

gs.GAME_CHARACTER = "+"
gs.OBSTACLE_CHARACTER = "#"

#! The game starts only if this file is executed
if __name__ == '__main__':
    game.show_game()
    with gs.Listener(on_press=controls.on_press, on_release=controls.on_release) as listener:
        listener.join()