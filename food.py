import settings as gs
import player

foods = []

class Food:
    def __init__(self, food_character):        
        self.x_pos = gs.random.randint(1, len(gs.gameboard[0])-2)
        self.y_pos = gs.random.randint(1, len(gs.gameboard)-2)
        self.character = food_character


def generate_food(amount):    
    if len(foods) == 0:
        gs.ROUND += 1
        
        for _ in range(0, amount):
            positions = []
            for y in foods:
                positions.append(y.y_pos)

            if not _ >= len(gs.gameboard)-2:    # -2 for the top and bottom borders
                while True:
                    food = Food(gs.FOOD_CHARACTER)
                    if food.y_pos not in positions and food.y_pos != player.player.y_pos:
                        foods.append(food)
                        break

#! Don't change the code below this line
if __name__ == '__main__':
    exit()