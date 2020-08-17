import settings as gs
import controls
import obstacle

class Game:
    def __init__(self, x, y, player_character):
        self.x_pos = gs.math.ceil(x)     #! } Position must be an integer
        self.y_pos = gs.math.ceil(y)     #! }
        self.player = player_character

        self.gameboard = gs.gameboard           # The map is in the settings(.py)
        self.map_width = len(self.gameboard[0]) # Get the map's width by the first element in the gameboard list
        self.map_height = len(self.gameboard)

    def show_game(self):
        gs.clear()
        obstacle.create_obstacles(3)

        for i in range(0, self.map_height):
            line = ""
            player_in_line = False
            obstacle_in_line = False

            for j, map_piece in enumerate(self.gameboard[i]):
                for obs in obstacle.obstacles:
                    if j == obs.x_pos and i == obs.y_pos:
                        if obs.is_alive:
                            obstacle_in_line = True

                        # Draw the obstacle
                        if self.x_pos == obs.x_pos and self.y_pos == obs.y_pos:
                            obs.is_alive = False
                            gs.SCORE += 1
                            obstacle.obstacles.remove(obs)
                        else:
                            if obs.is_alive:
                                line += gs.obstacle_color + obs.character + gs.reset + gs.bg_color + gs.border_color

                if j == self.x_pos and i == self.y_pos:
                    player_in_line = True
                    
                    # Draw the player
                    line += gs.bold + gs.player_color + self.player + gs.reset + gs.bg_color + gs.border_color

                else:
                    line += map_piece

            #! Removin and adding parts to the string, to remove the gap which appears
            #! when the player is in the same line as the obstacle     
            if player_in_line and obstacle_in_line == False:
                line += "|"
                
            if player_in_line and obstacle_in_line:
                line = line[:-1]
                line += "|"

            if player_in_line or obstacle_in_line:
                line = line[:-2]                      
                line += "|"            

            #! Coloring the string after it's done to avoid messing with the ASCII color codes
            line += gs.border_color + gs.reset
            print(gs.bg_color + gs.border_color + line + gs.reset)
        print(f"{gs.green}Score: {gs.reset}{gs.SCORE}")
        print(f"x:{self.x_pos} y:{self.y_pos}\n")     # Print the player's position                  

    def player_dir(self, x_dir, y_dir):
        self.x_pos += x_dir
        self.y_pos += y_dir
        self.show_game()


game = Game(0.1, 1, gs.GAME_CHARACTER)  # Player position and character (in: settings.py)

#! The game starts only if this file is executed
#! Don't change the code below this line
if __name__ == '__main__':
    game.show_game()
    with gs.Listener(on_press=controls.on_press, on_release=controls.on_release) as listener:
        listener.join()