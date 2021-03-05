from random import randint

game_on = True

while game_on:

    # various positions on the game board
    pos_1 = " "
    pos_2 = " "
    pos_3 = " "
    pos_4 = " "
    pos_5 = " "
    pos_6 = " "
    pos_7 = " "
    pos_8 = " "
    pos_9 = " "

    occupied_pos = []  # a list of all occupied positions on the game board

    def print_game_board():
        """A function that prints out the Tic Tac Toe game board"""

        print()
        print(f" {pos_1} | {pos_2} | {pos_3}"
              f"\n___________\n "
              f"{pos_4} | {pos_5} | {pos_6}"
              f"\n___________\n "
              f"{pos_7} | {pos_8} | {pos_9}")
        print()

    def game_move(user_move, user_choice):
        """A function that places a user's symbol on the selected position"""

        global pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8, pos_9

        if user_move == 1:
            pos_1 = user_choice
        elif user_move == 2:
            pos_2 = user_choice
        elif user_move == 3:
            pos_3 = user_choice
        elif user_move == 4:
            pos_4 = user_choice
        elif user_move == 5:
            pos_5 = user_choice
        elif user_move == 6:
            pos_6 = user_choice
        elif user_move == 7:
            pos_7 = user_choice
        elif user_move == 8:
            pos_8 = user_choice
        elif user_move == 9:
            pos_9 = user_choice

    def check_winner():
        """A function that checks across the whole game board and returns the winning symbol"""

        if pos_1 == "X" and pos_2 == "X" and pos_3 == "X":
            return "X"
        elif pos_4 == "X" and pos_5 == "X" and pos_6 == "X":
            return "X"
        elif pos_7 == "X" and pos_8 == "X" and pos_9 == "X":
            return "X"
        elif pos_1 == "X" and pos_5 == "X" and pos_9 == "X":
            return "X"
        elif pos_3 == "X" and pos_5 == "X" and pos_7 == "X":
            return "X"
        elif pos_1 == "X" and pos_4 == "X" and pos_7 == "X":
            return "X"
        elif pos_2 == "X" and pos_5 == "X" and pos_8 == "X":
            return "X"
        elif pos_3 == "X" and pos_6 == "X" and pos_9 == "X":
            return "X"

        elif pos_1 == "O" and pos_2 == "O" and pos_3 == "O":
            return "O"
        elif pos_4 == "0" and pos_5 == "O" and pos_6 == "O":
            return "O"
        elif pos_7 == "O" and pos_8 == "O" and pos_9 == "O":
            return "O"
        elif pos_1 == "O" and pos_5 == "O" and pos_9 == "O":
            return "O"
        elif pos_3 == "O" and pos_5 == "O" and pos_7 == "O":
            return "O"
        elif pos_1 == "O" and pos_4 == "O" and pos_7 == "O":
            return "O"
        elif pos_2 == "O" and pos_5 == "O" and pos_8 == "O":
            return "O"
        elif pos_3 == "O" and pos_6 == "O" and pos_9 == "O":
            return "O"

    start_game = input("Do you want to play a game of Tic Tac Toe (y/n)? ").lower()

    if start_game == "y":

        print_game_board()
        player_choice = input("X or O? ").upper()

        if player_choice == "X" or player_choice == "O":

            if player_choice == "X":
                comp = "O"
                print()
                print("Computer will be O")  # informing the user they will be playing against an AI computer
                print()
            elif player_choice == "O":
                comp = "X"
                print()
                print("Computer will be X")
                print()

            while len(occupied_pos) < 9:

                try:
                    player_move = int(input(f"Pick a position to place {player_choice} on the game board from 1-9? "))
                except ValueError:
                    print()
                    print("That's not a number! Pick a valid number from 1-9!")
                    print()
                    continue
                else:

                    if player_move in occupied_pos:
                        print()
                        print("That position has been occupied! Select another one")
                        print()
                        continue

                    game_move(player_move, player_choice)
                    occupied_pos.append(player_move)

                    # Check if the player has won the game
                    if check_winner() == "X" and player_choice == "X":
                        print_game_board()
                        print("Game Over! You won!")
                        print()
                        break
                    elif check_winner() == "O" and player_choice == "O":
                        print_game_board()
                        print("Game Over! You won!")
                        print()
                        break

                    # end the game once all positions have been occupied without a winner
                    if len(occupied_pos) == 9:
                        print_game_board()
                        print("Game over! It's a tie")
                        break

                    else:
                        comp_move = randint(1, 9)

                        # computer must reselect another position until it gets an unoccupied position on the game board
                        while comp_move in occupied_pos:
                            comp_move = randint(1, 9)

                        game_move(comp_move, comp)
                        occupied_pos.append(comp_move)

                        # Check if the computer has won the game
                        if check_winner() == "X" and comp == "X":
                            print_game_board()
                            print("Game Over! You lost! Computer won!")
                            print()
                            break
                        elif check_winner() == "O" and comp == "O":
                            print_game_board()
                            print("Game Over! You lost! Computer won!")
                            print()
                            break

                        print_game_board()
        else:
            print()
            print("Wrong letter! Choose 'X' or 'O'")
            print()
    else:
        game_on = False
