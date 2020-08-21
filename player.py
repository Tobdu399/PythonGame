import settings as gs
import food

class Player:
    def __init__(self, x, y, player_character):
        self.x_pos = gs.math.ceil(x)     #! } Position must be an integer
        self.y_pos = gs.math.ceil(y)     #! }
        self.player = player_character

        self.gameboard = gs.gameboard           # The map is in the settings(.py)
        self.map_width = len(self.gameboard[0]) # Get the map's width by the first element in the gameboard list
        self.map_height = len(self.gameboard)

    def show_game(self):
        gs.clear()
        food.generate_food(gs.FOOD_AMOUNT)

        for i in range(0, self.map_height):
            line = ""
            player_in_line = False
            food_in_line = False

            for j, map_piece in enumerate(self.gameboard[i]):
                for food_obj in food.foods:
                    if j == food_obj.x_pos and i == food_obj.y_pos:
                        if food_obj.is_alive:
                            food_in_line = True

                        #! Draw the food
                        if self.x_pos == food_obj.x_pos and self.y_pos == food_obj.y_pos:
                            food_obj.is_alive = False
                            gs.SCORE += (1 / gs.ROUND)  #! Score increment
                            food.foods.remove(food_obj)
                        else:
                            if food_obj.is_alive:
                                line += gs.food_color + food_obj.character + gs.reset + gs.bg_color + gs.border_color

                if j == self.x_pos and i == self.y_pos:
                    player_in_line = True
                    
                    #! Draw the player
                    line += gs.bold + gs.player_color + self.player + gs.reset + gs.bg_color + gs.border_color

                else:
                    line += map_piece

            #! Removin and adding parts to the string, to remove the gap which appears
            #! when the player is in the same line as the food     
            if player_in_line and food_in_line == False:
                line += "|"
                
            if player_in_line and food_in_line:
                line = line[:-1]
                line += "|"

            if player_in_line or food_in_line:
                line = line[:-2]                      
                line += "|"            

            #! Coloring the string after it's done to avoid messing with the ASCII color codes
            line += gs.border_color + gs.reset
            print(gs.bg_color + gs.border_color + line + gs.reset)
            
        # Formatting the score to 1 decimal
        print(f"{gs.green}Score: {gs.reset}{gs.SCORE:.1f}") #! }
        print(f"{gs.green}Round: {gs.reset}{gs.ROUND}")     #! } Player's score, round, and location
        print(f"x:{self.x_pos} y:{self.y_pos}\n")           #! }

    def player_dir(self, x_dir, y_dir):
        self.x_pos += x_dir
        self.y_pos += y_dir
        self.show_game()

#! Don't change the code below this line!
player = Player(1, 1, gs.GAME_CHARACTER)
if __name__ == '__main__':
    exit()