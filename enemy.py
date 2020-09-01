import settings as gs
import player

enemies = []

class Enemy:
    def __init__(self):
        self.x_pos = 1 if gs.random.random() < 0.5 else len(gs.gameboard[0])-2
        self.y_pos = gs.random.randint(1, len(gs.gameboard)-2)
        self.character = "C" if self.x_pos == 1 else "Ɔ"
        self.direction = 1 if self.x_pos == 1 else -1
        
    def move(self):
        if self.x_pos == 1 and self.direction == -1:
            self.character = "C"
            self.direction = 1
        if self.x_pos == len(gs.gameboard[0])-2 and self.direction == 1:
            self.character = "Ɔ"
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
                    if enemy.y_pos not in positions and enemy.y_pos != player.player.y_pos:
                        enemies.append(enemy)
                        break

def update():
    while gs.GAME:
        for enemy in enemies:
            enemy.move()
        
        player.player.show_game()
        gs.time.sleep(0.5)