from . import settings as gs
from . import player

enemies = []
just_spawned = False

class Enemy:
    def __init__(self):
        # self.x_pos = 1 if gs.random.random() < 0.5 else len(gs.gameboard[0])-2
        self.x_pos = gs.random.randint(1, len(gs.gameboard[0])-2)

        self.y_pos = gs.random.randint(1, len(gs.gameboard)-2)
        self.character = gs.ENEMY_CHARACTER[0] if self.x_pos == 1 else gs.ENEMY_CHARACTER[1]
        self.direction = 1 if self.x_pos == 1 else -1

    def move(self):
        if self.x_pos == 1 and self.direction == -1:
            self.character = gs.ENEMY_CHARACTER[0]
            self.direction = 1
        if self.x_pos == len(gs.gameboard[0])-2 and self.direction == 1:
            self.character = gs.ENEMY_CHARACTER[1]
            self.direction = -1
        self.x_pos += self.direction

def generate_enemies(amount):
    global just_spawned
    if len(enemies) == 0:
        for _ in range(0, amount):
            positions = []
            for y in enemies:
                positions.append(y.y_pos)

            if not _ >= len(gs.gameboard)-2:
                while True:
                    enemy = Enemy()
                    if enemy.y_pos not in positions and enemy.y_pos != player.player.y_pos and enemy.x_pos != player.player.x_pos:
                        enemies.append(enemy)
                        break
        just_spawned = True

def increase_speed():
    if gs.ROUND % 5 == 0:
        if gs.REFRESH_RATE > 0.06:
            gs.REFRESH_RATE -= 0.05

def update():
    global just_spawned
    while gs.GAME:        
        if just_spawned:
            gs.time.sleep(gs.SPAWNING_RATE)
            just_spawned = False
        else:
            gs.time.sleep(gs.REFRESH_RATE)
            
        for enemy in enemies:
            enemy.move()
            
        player.player.show_game()

if __name__ == '__main__':
    exit()