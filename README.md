# PaperAndPencilGame
This is simple console game - Paper and pencil rom SoftUni Advanced course with Python

![image](https://github.com/IvanVakov/PaperAndPencilGame/assets/119103300/69b309c8-8e67-4ffd-aa20-fac7f9ea3379)

This code is a Python implementation of a paper and pencil game, commonly known as Tic-Tac-Toe. The code uses several libraries:

speech_recognition: Allows the program to listen to speech input and recognize the player's name using Google's speech recognition service.
collections: Provides the deque data structure, which is used to rotate between players.
pyfiglet: Enables the rendering of ASCII art text using different fonts.
colorama: Provides colored output in the console.
The main functionality of the code includes:

get_name(player_number): Uses speech recognition to prompt each player to say their name and returns the recognized name as a string.
check_for_win(): Checks if the current player has won the game by examining the game board for winning conditions (diagonals, rows, columns).
place_symbol(row, col): Places the current player's symbol (X or O) on the game board at the specified row and column. It calls check_for_win() to check for a win and then prints the updated game board.
choose_position(): Prompts the current player to choose a position on the game board and validates their input. If the input is valid and the position is free, it calls place_symbol() to place the symbol on the board.
print_game_board(begin=False): Prints the current state of the game board. If begin is True, it also displays the initial numbering of the board. This function is used to display the board at various stages of the game.
start(): Initializes the game by getting the names and symbols of the two players, printing the initial game board, and starting the game loop.
ask_restart(): Asks the players if they want to restart the game. If they answer "yes," it calls start() to restart the game. If they answer "no," it exits the program.
The code also defines some constants and variables:

SIZE: The size of the game board (default is 3x3).
turns: The number of turns played in the game.
game_board: A 2D list representing the game board.
players: A deque to store the player names and symbols. It allows for easy rotation between players.
The program starts by calling the start() function, which initiates the game.

Example screenshots from the game:

![image](https://github.com/IvanVakov/PaperAndPencilGame/assets/119103300/da6ffa0e-ecef-413c-b9bf-a2fcd10375a3)

![image](https://github.com/IvanVakov/PaperAndPencilGame/assets/119103300/8027bd95-49ea-41b1-821f-52d2431e4c1c)

# Live Demo

You can play the game directly in your Web browser here:

# first open <a href="https://replit.com/@Ivakov/Paper-and-pencil-game#main.py">this link<a/>
  
![image](https://github.com/IvanVakov/PaperAndPencilGame/assets/119103300/5e8bb191-002d-4a7c-bf7e-c58132917bc9)
 
![image](https://github.com/IvanVakov/PaperAndPencilGame/assets/119103300/55e5300f-732e-4227-a1e7-9d2a33c40e8a)
