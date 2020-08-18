import sourcedefender
import settings as gs
from player import player
import controls

gs.GAME_CHARACTER = "+"
gs.FOOD_CHARACTER = "#"
gs.FOOD_AMOUNT = 3

#! Advanced
gs.CLEAR_COMMAND = "clear"

#! The game starts only if this file is executed
if __name__ == '__main__':
    player.show_game()
    with gs.Listener(on_press=controls.on_press, on_release=controls.on_release) as listener:
        listener.join()