from lib import settings as gs, controls, food, enemy
from lib.player import player

# Settings
gs.PLAYER_CHARACTER   = "+"
gs.OBSTACLE_CHARACTER = "#"
gs.ENEMY_CHARACTER    = ("C", "Ɔ")
gs.FOOD_AMOUNT        = 5
gs.ENEMY_AMOUNT       = 4

# Advanced settings
gs.SCORE              = 0
gs.ROUND              = 0
gs.REFRESH_RATE       = 0.49
gs.SPAWNING_RATE      = 1.5

# The game starts only if this file is executed
if __name__ == '__main__':
    listener = gs.Listener(on_press=controls.on_press, on_release=controls.on_release)
    player.show_game()

    listener.start()                                    # Start the keyboard listener
    gs.threading.Thread(target = enemy.update).start()  # Update the position of the enemies
