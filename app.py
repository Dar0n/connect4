import random

class Game:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.turn = 1

    def setUp(self):
        self.board = Board(self.board_width, self.board_height)
        self.computer_player1 = ComputerPlayer(self.board_width, 1)
        self.computer_player2 = ComputerPlayer(self.board_width, 2)
        self.play()

    def play(self):
        step = 0
        while step < 100:
            step += 1
            # if self.turn == 1:
            #     player = self.computer_player1
            #     self.turn = 2
            # else:
            #     player = self.computer_player2
            #     self.turn = 1
            player = self.computer_player1
            self.board.throw_coin(player.make_move(), player.number)
            self.board.draw_matrix()
            if self.board.check_win_row():
                print('Player 1 won')
                break
            print('=====')


class ComputerPlayer:
    def __init__(self, width, number):
        self.board_width = width
        self.number = number

    def make_move(self):
        return random.randint(0, self.board_width)

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = self.build_board()
        self.last_move = [-1, -1, -1]

    def build_board(self):
        matrix = [
            [0 for x in range(self.height)]
            for y in range(self.width)
        ]
        return matrix

    def draw_matrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def throw_coin(self, column, number):
        if self.matrix[0][column] != 0:
            return False
        for i in reversed(range(len(self.matrix))):
            if self.matrix[i][column] == 0:
                self.matrix[i][column] = number
                self.last_move = [i, column, number]
                return True

    def check_win_row(self):
        row = self.last_move[0]
        counter = 0
        for i in range(1, len(self.matrix[row])):
            if self.matrix[row][i] == self.matrix[row][i-1] == self.last_move[2]:
                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 0
        return False




# board = Board(5,6)
# board.throw_coin(3)
# board.throw_coin(3)
# board.draw_matrix()
game = Game(5,6)
game.setUp()