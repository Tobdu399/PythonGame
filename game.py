import settings as gs
import controls

GAME_CHARACTER = "+"

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

        for i in range(0, self.map_height):
            line = ""
            bg_color = gs.black_bg
            border_color = gs.blue
            player_color = gs.yellow

            player_in_line = False

            for j, map_piece in enumerate(self.gameboard[i]):
                if j == self.x_pos and i == self.y_pos:
                    player_in_line = True
                    line += gs.bold + player_color + self.player + gs.reset + bg_color  # Draw the player
                
                line += map_piece

            if player_in_line:
                line = line[:-2]   # Removin the gap that appears when the player is in the line            
                line += border_color + "|" + gs.reset   # Adding the border back after removing it in the line above

            print(bg_color + border_color + line + gs.reset)
        print(f"x:{self.x_pos} y:{self.y_pos}\n")       # Print the player's position                  

    def player_dir(self, x_dir, y_dir):
        self.x_pos += x_dir
        self.y_pos += y_dir
        self.show_game()


game = Game(1, 1, GAME_CHARACTER)  # Player position and character

# Don't change the code below this line
if __name__ == '__main__':
    game.show_game()
    with gs.Listener(on_press=controls.on_press, on_release=controls.on_release) as listener:
        listener.join()