import random

class TicTacToe:

    # initializing empty board
    def __init__(self):
        self.board = []

    # creating empty board
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    # computer determines Player X or Player O goes first
    def get_random_first_player(self):
        return random.randint(0, 1)

    # user inputs mark on board using the format of rows and then columns (ie 1 1 for row 1 column 1)
    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    # to determine which player wins
    def did_player_win(self, player):
        win = None

        n = len(self.board)

        # to check rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # to check columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # to check diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    # to determine if board is filled
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    # to show the board to players
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # to start the game
    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # to take user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # to fix the spot
            self.fix_spot(row - 1, col - 1, player)

            # to check if current player won
            if self.did_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # to check if current player won
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
