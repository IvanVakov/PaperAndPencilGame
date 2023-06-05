import speech_recognition as sr
from collections import deque
from pyfiglet import Figlet
from colorama import Fore


def get_name(player_number):
    while True:
        with sr.Microphone() as microphone:
            r = sr.Recognizer()
            print(f"Player {player_number} please say your name:")

            audio = r.record(microphone, duration=3)
            print("Recognizing...")

            try:
                return r.recognize_google(audio)
            except sr.exceptions.UnknownValueError:
                print("Please say your name again")


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([game_board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([game_board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])
    row_win = any([all(player_symbol == position for position in row) for row in game_board])
    col_win = any([all(game_board[row][col] == player_symbol for row in range(SIZE)) for col in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_game_board()
        print(f"{player_name} won!")
        ask_restart()


def place_symbol(row, col):
    game_board[row][col] = players[0][1]

    check_for_win()
    print_game_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        ask_restart()

    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(
                input(f"{players[0][0]} please choose a free position in the range between [1-{SIZE * SIZE}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print(Fore.RED + f"{players[0][0]}, please select a valid position!" + Fore.RESET)
            continue
        if 1 <= position <= SIZE * SIZE and game_board[row][col] == " ":
            turns += 1
            place_symbol(row, col)
        else:
            print(Fore.RED + f"{players[0][0]}, please select a valid position!" + Fore.RESET)


def print_game_board(begin=False):
    if begin:
        print("This is the numeration of the game board:")
        [print(f"| {' | '.join(row)} |") for row in game_board]

        for row in range(SIZE):
            for col in range(SIZE):
                game_board[row][col] = " "
    else:
        [print(f"| {' | '.join(row)} |") for row in game_board]


def start():
    figlet = Figlet(font="Small")
    print(figlet.renderText("Paper and pencil game"))

    player_one_name = Fore.RED + get_name("one") + Fore.RESET
    player_two_name = Fore.BLUE + get_name("two") + Fore.RESET
    # player_one_name = input("Player one, please choose your name: ")
    # player_two_name = input("Player two, please choose your name: ")
    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

        if player_one_symbol not in ["X", "O"]:
            print(Fore.RED + f"{player_one_name} please choose a valid symbol!" + Fore.RESET)
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, Fore.RED + player_one_symbol + Fore.RESET])
    players.append([player_two_name, Fore.BLUE + player_two_symbol + Fore.RESET])

    print_game_board(begin=True)
    choose_position()


def ask_restart():
    while True:
        restart = input("Do you want to restart the game? (yes/no): ").lower()
        if restart == "yes":
            start()
        elif restart == "no":
            print("Thank you for playing! Goodbye!")
            raise SystemExit
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


SIZE = 3
turns = 0
game_board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, SIZE * SIZE, SIZE)]
players = deque()

start()
