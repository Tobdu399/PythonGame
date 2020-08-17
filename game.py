import settings as gs
import controls
import obstacle

class Game:
    def __init__(self, x, y, player_character):
        self.x_pos = x
        self.y_pos = y
        self.player = player_character

        self.gameboard = gs.gameboard           # The map is in the settings(.py)
        self.map_width = len(self.gameboard[0]) # Get the map's width by the first element in the gameboard list
        self.map_height = len(self.gameboard)

    def show_game(self):
        gs.clear()

        bg_color = gs.black_bg
        border_color = gs.blue
        player_color = gs.yellow
        obstacle_color = gs.red

        obstacle.generate_obstacles(3)

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
                        else:
                            if obs.is_alive:
                                line += obstacle_color + obs.character + gs.reset + bg_color + border_color

                if j == self.x_pos and i == self.y_pos:
                    player_in_line = True
                    
                    # Draw the player
                    line += gs.bold + player_color + self.player + gs.reset + bg_color + border_color

                else:
                    line += map_piece

            if player_in_line and obstacle_in_line == False:
                line += "|"

            if player_in_line or obstacle_in_line:
                line = line[:-2]                        # Removin the gap that appears when the player is in the line
                line += "|"                             # Adding the border back after removing it in the line above            

            if player_in_line and obstacle_in_line:
                line = line[:-1]
                line += "|"

            line += border_color + gs.reset   
            print(bg_color + border_color + line + gs.reset)
        print(f"x:{self.x_pos} y:{self.y_pos}\n")       # Print the player's position                  

    def player_dir(self, x_dir, y_dir):
        self.x_pos += x_dir
        self.y_pos += y_dir
        self.show_game()


game = Game(1, 1, gs.GAME_CHARACTER)  # Player position and character

# Don't change the code below this line
if __name__ == '__main__':
    game.show_game()
    with gs.Listener(on_press=controls.on_press, on_release=controls.on_release) as listener:
        listener.join()
