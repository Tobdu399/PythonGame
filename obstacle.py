import settings as gs
obstacles = []

class Obstacle:
    def __init__(self, obstacle_character):
        self.character = obstacle_character
        
        self.x_pos = gs.random.randint(1, len(gs.gameboard[0])-2)
        self.y_pos = gs.random.randint(1, len(gs.gameboard)-2)
        self.is_alive = True


for _ in range(0, 3):   # Amount of the obstacles (max: the number of rows on the map)
    positions = []
    for y in obstacles:
        positions.append(y.y_pos)

    # Only one obstacle can be in a line
    if not _ >= len(gs.gameboard)-2:    # -2 for the top and bottom borders
        while True:
            obstacle = Obstacle(gs.OBSTACLE_CHARACTER)
            if obstacle.y_pos not in positions:
                obstacles.append(obstacle)
                break

# Don't change the code below this line
if __name__ == '__main__':
    print(gs.wrong_file_msg + __file__)
    exit()