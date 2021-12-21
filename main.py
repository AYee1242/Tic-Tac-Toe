from tic_tac_toe import TicTacToe


def main():
    try:
        print("Welcome to tic tac toe!")
        rows = int(input("How many rows does the board have? "))
        columns = int(input("How many columns does the board have? "))
        win_cond = int(input("How many matches for a win? "))
        tic_tac_toe = TicTacToe(rows, columns, win_cond)
        tic_tac_toe.play_game()
    except ValueError as e:
        print(e)


# Executes the main function
if __name__ == '__main__':
    main()
