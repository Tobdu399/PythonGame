import settings as gs
import food
import enemy

class Player:
    def __init__(self, x, y, player_character):
        self.x_pos = gs.math.ceil(x)     #! } The position must be an integer
        self.y_pos = gs.math.ceil(y)     #! }
        self.character = player_character

        self.gameboard = gs.gameboard           # The map is in the settings(.py)
        self.map_width = len(self.gameboard[0]) # Get the map's width by the first element in the gameboard list
        self.map_height = len(self.gameboard)

    def show_game(self):
        gs.clear()
        
        food.generate_food(gs.FOOD_AMOUNT)
        enemy.generate_enemies(3)

        for i in range(0, self.map_height):
            line = ""

            # Looping through every character in the map
            for j, map_piece in enumerate(self.gameboard[i]):
                # Food
                for food_obj in food.foods:
                    if j == food_obj.x_pos and i == food_obj.y_pos:
                        if self.x_pos == food_obj.x_pos and self.y_pos == food_obj.y_pos:
                            gs.SCORE += (1 / gs.ROUND)  #! Score increment
                            food.foods.remove(food_obj)
                        else:
                            map_piece = gs.food_color + food_obj.character + gs.reset + gs.bg_color + gs.border_color                               

                # Enemy
                for enemy_obj in enemy.enemies:                  
                    if j == enemy_obj.x_pos and i == enemy_obj.y_pos:
                        if self.x_pos == enemy_obj.x_pos and self.y_pos == enemy_obj.y_pos:
                            enemy.enemies.remove(enemy_obj)
                            # TODO: health system
                        else:
                            map_piece = gs.enemy_color + enemy_obj.character + gs.reset + gs.bg_color + gs.border_color

                # Player
                if j == self.x_pos and i == self.y_pos:
                    map_piece = gs.bold + gs.player_color + self.character + gs.reset + gs.bg_color + gs.border_color

                line += map_piece

            #! Coloring the string after it's done to avoid messing with the ASCII color codes
            line += gs.border_color + gs.reset
            print(gs.bg_color + gs.border_color + line + gs.reset)
            
        # Formatting the score to one decimal
        print(f"{gs.green}Score: {gs.reset}{gs.SCORE:.1f}") #! }
        print(f"{gs.green}Round: {gs.reset}{gs.ROUND}")     #! } Player's score, round, and location
        print(f"x:{self.x_pos} y:{self.y_pos}\n")           #! }

    def player_dir(self, x_dir, y_dir):
        self.x_pos += x_dir
        self.y_pos += y_dir
        self.show_game()

#! Don't change the code below this line!
player = Player(1, 1, gs.PLAYER_CHARACTER)
if __name__ == '__main__':
    exit()
