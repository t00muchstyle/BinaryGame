
from BinaryConverterGame.Game import BinaryGame

game = BinaryGame()

while game.running:
    game.curr_menu.display_menu()
    game.game_loop()
