import sourcedefender
import settings as gs
import controls
import food
from player import player

gs.GAME_CHARACTER = "+"
gs.OBSTACLE_CHARACTER = "#"
gs.FOOD_AMOUNT = 5

#! Advanced
gs.CLEAR_COMMAND = "clear"
gs.SCORE = 0
gs.ROUND = 0

#! The game starts only if this file is executed
if __name__ == '__main__':
    player.show_game()
    with gs.Listener(on_press=controls.on_press, on_release=controls.on_release) as listener:
        listener.join()
