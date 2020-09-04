import settings as gs
import player

enemies = []

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
    if len(enemies) == 0:
        for _ in range(0, amount):
            positions = []
            for y in enemies:
                positions.append(y.y_pos)

            if not _ >= len(gs.gameboard)-2:
                while True:
                    enemy = Enemy()
                    if enemy.y_pos not in positions:
                        enemies.append(enemy)
                        break

def increase_speed():
    if gs.ROUND % 5 == 0:
        if gs.REFRESH_RATE > 0.06:
            gs.REFRESH_RATE -= 0.05

def update():            
    while gs.GAME:
        for enemy in enemies:
            enemy.move()

        player.player.show_game()
        gs.time.sleep(gs.REFRESH_RATE)
