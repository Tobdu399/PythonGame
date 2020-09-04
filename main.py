import settings as gs
import controls
import food
from player import player
import enemy

gs.PLAYER_CHARACTER   = "+"
gs.OBSTACLE_CHARACTER = "#"
gs.ENEMY_CHARACTER    = ["C", "Ɔ"]
gs.FOOD_AMOUNT        = 5
gs.ENEMY_AMOUNT       = 4

gs.SCORE = 0
gs.ROUND = 0

# The game starts only if this file is executed
listener = gs.Listener(on_press=controls.on_press, on_release=controls.on_release)
if __name__ == '__main__':
    player.show_game()
    listener.start()
    gs.threading.Thread(target = enemy.update).start()