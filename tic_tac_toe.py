import ast


class TicTacToe:
    def __init__(self, row: int, column: int, winCon: int):
        """
        Create a TicTacToe game

        :int row: The number of rows on the board
        :int column: The number of columns in each row
        :int winCon: How many marks required to win
        :raises ValueError: if the row, column or winCon is not a positive number
        """

        if row <= 0:
            raise ValueError('Row must be a positive number')

        if column <= 0:
            raise ValueError('Column must be a positive number')

        if winCon <= 0:
            raise ValueError('WinCon must be a positive number')

        self.num_rows = row
        self.num_columns = column
        self.win_con = winCon
        self.player = 'X'
        self.board = [[' ' for i in range(column)] for j in range(row)]

    def print_board(self):
        # Formatting the index display
        print(" ", end="")
        for idx in range(self.num_columns):
            print(f" {idx}  ", end="")
        print("")
        for idx, row in enumerate(self.board):
            print(f"{idx} ", end="")
            # Last column does not need to end with |
            for val in row[:-1]:
                print(val, end=" | ")

            # Last value in the row
            print(row[-1])
            if idx != len(self.board) - 1:
                # Split new rows
                print(" ", end="")
                for i in range(self.num_columns - 1):
                    print("---+", end="")
                print("---")

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == ' ':
                    return False
        return True

    def player_won(self):
        # horizontal check
        for row in range(self.num_rows):
            for column in range(self.num_columns - self.win_con + 1):
                is_winner = True
                for i in range(column, column + self.win_con):
                    if (self.board[row][i] != self.player):
                        is_winner = False
                        break
                if is_winner:
                    return True

        # vertical check
        for row in range(self.num_rows - self.win_con + 1):
            for column in range(self.num_columns):
                is_winner = True
                for i in range(row, row + self.win_con):
                    if (self.board[i][column] != self.player):
                        is_winner = False
                        break
                if is_winner:
                    return True

        # ascending diagonal check
        for row in range(self.win_con - 1, self.num_rows):
            for column in range(self.num_columns - self.win_con + 1):
                is_winner = True
                for i in range(self.win_con):
                    if (self.board[row - i][column + i] != self.player):
                        is_winner = False
                        break
                if is_winner:
                    return True

        # descending diagonal check
        for row in range(self.num_rows - self.win_con + 1):
            for column in range(self.num_columns - self.win_con + 1):
                is_winner = True
                for i in range(self.win_con):
                    if (self.board[row + i][column + i] != self.player):
                        is_winner = False
                        break
                if is_winner:
                    return True

        return False

    def play_game(self):
        while True:
            self.print_board()

            print(f"It's your turn player {self.player}")

            # Getting player input
            while True:
                move = ast.literal_eval(
                    input("Enter a coordinate in the form of row,column (eg: 0,0): "))
                if move[0] < 0 or move[0] >= self.num_rows or move[1] < 0 or move[1] >= self.num_columns:
                    print("That move is out of bounds! Please try again")
                elif self.board[move[0]][move[1]] != ' ':
                    print("This place is already taken! Please try again")
                else:
                    break

            self.board[move[0]][move[1]] = self.player

            # if a player meets the required matches, they win
            if self.player_won():
                self.print_board()
                print(f"Game Over, player {self.player} wins!")
                break

            # if the board is comepletely full, then it is a tie
            if self.is_board_filled():
                self.print_board()
                print("Game over, it is a tie!")
                break

            self.player = 'O' if self.player == 'X' else 'X'
