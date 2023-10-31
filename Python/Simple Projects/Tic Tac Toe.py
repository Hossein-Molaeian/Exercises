import random


"""
1- Write a function that can print out a board. Set up your board as a list,
where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
"""


def display_board(board):
    print("\n"*5)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])


"""
2- Write a function that can take in a player input and assign their marker as 'X' or 'O'.
Think about using *while* loops to continually ask until you get a correct answer.
"""


def player_input():
    marker = " "
    while marker not in ["X", "O"]:
        marker = input("Player 1: Choose your marker (X/O): ")
        if marker.upper() == "X":
            return ("X", "O")
        elif marker.upper() == "O":
            return ("O", "X")
        else:
            print("That is not a valid marker. Try again.")


"""
3- Write a function that takes in the board list object,
a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
"""


def place(board, marker, index):
    board[index] = marker


"""
4- Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
"""


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


"""
5- Write a function that uses the random module to randomly decide which player goes first.
You may want to lookup random.randint() Return a string of which player went first.
"""


def player_turn():
    if random.randint(0, 1) == 0:
        return "Player 2"
    return "Player 1"


"""
6- Write a function that returns a boolean indicating whether a space on the board is freely available.
"""


def space_check(board, index):
    return board[index] == " "


"""
7- Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
"""


def full_check(board):
    for i in range(1, len(board)):
        if space_check(board, i):
            return False
    return True


"""
8- Write a function that asks for a player's next position (as a number 1-9)
and then uses the function from step 6 to check if it's a free position.
If it is, then return the position for later use.
"""


def player_choice(board):
    position = 0
    check = True
    while check:
        try:
            position = int(input("Choose your next position: (1-9): "))
            if position not in range(1, 10):
                print("You are out of range. Try again. ")
            elif not space_check(board, position):
                print("That position is already full. Try again. ")
            elif position in range(1, 10) and space_check(board, position):
                check = False
                return position
        except ValueError:
            print("Please input a number between 1 and 9. ")


"""
9- Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
"""


def replay():
    return input("Do you want to play again? (Y/N): ").upper().startswith("Y")


"""
10- Use while loops and the functions you've made to run the game!
"""

print("Welcome to Tic Tac Toe")

while True:
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()
    print(
        f"Player 1's marker is '{player1_marker}' and Player 2's marker is '{player2_marker}'")
    question = " "
    turn = player_turn()
    print(f"{turn} will go first.")
    while question not in ["Y", "N"]:
        question = input("Are you ready to play? (Y/N): ")
        if question.upper() == "Y":
            game_on = True
            question = "Y"
        elif question.upper() == "N":
            game_on = False
            break
        else:
            print("Please indicate Y or N: ")
            game_on = False

        while game_on:
            if turn == "Player 1":
                display_board(the_board)
                position = player_choice(the_board)
                place(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print("Player 1: Congratulations! You have won the game")
                    game_on = False
                elif full_check(the_board):
                    display_board(the_board)
                    print("The game is a tie!")
                    game_on = False
                else:
                    turn = "Player 2"
            else:
                display_board(the_board)
                position = player_choice(the_board)
                place(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Player 2: Congratulations! You have won the game")
                    game_on = False
                elif full_check(the_board):
                    display_board(the_board)
                    print("The game is a tie!")
                    game_on = False
                else:
                    turn = "Player 1"
    if not replay():
        break
