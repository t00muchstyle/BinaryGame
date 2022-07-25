import random
class Board():
    def __init__(self):
        boardList = [random.randrange(0, 1, 1) for i in range(8)]

    def display_board(self, boardList):
        print("Random number list is : " + str(boardList))
        return boardList

