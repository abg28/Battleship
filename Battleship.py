# BATTLESHIP CODE

from random import randint

#Test comment

# FUNCTIONS

# Function that checks to see if you're trying to create a ship in a spot that already contains part of a ship;
# returns true if there is a conflict, false otherwise
def check_overlap(ships, row, col):
    for key in ships:
        if [row, col] in ships[key][1]:
            return True
    return False


# Function that prints the board in a more aesthetically pleasing format
def print_board(board):
    print("   1 2 3 4 5 6 7 8 9 10")
    row_num = 1
    for row in board:
        if row_num != 10:
            print(str(row_num) + "  " + " ".join(row))
            row_num += 1
        else:
            print(str(row_num) + " " + " ".join(row))


# Function that populates the board with ships in random locations
def random_ship(board, ships, ship):
    while 1 == 1:

        break_out = True;

        # Makes sure the ship's coordinates reset for each iteration
        ships[ship][1] = []

        # Creates the first coordinate of the ship
        row = randint(0, len(board) - 1)
        col = randint(0, len(board[0]) - 1)
        if check_overlap(ships, row, col) == True:
            continue
        else:
            ships[ship][1].append([row, col])

            vert_or_horiz = randint(0, 1)

            # Horizontal case
            if vert_or_horiz == 0:
                for i in range(1, ships[ship][0]):
                    if check_overlap(ships, row + i, col) == True or row + i not in range(0, len(board) - 1):
                        break_out = False
                        break
                    else:
                        ships[ship][1].append([row + \
                                               i, col])

            if break_out == False:
                continue

            # Vertical case
            if vert_or_horiz == 1:
                for i in range(1, ships[ship][0]):
                    if check_overlap(ships, row, col + i) \
                            == True or col + i not in range(0, \
                                                            len(board[0]) - 1):
                        break_out = False
                        break
                    else:
                        ships[ship][1].append([row, col \
                                               + i])

            if break_out == False:
                continue
            elif break_out == True:
                break


##########################################################

##INITIALIZATIONS

# Creates empty board list
board = []

# Dictionary of ships that uses the ships' names as the keys and links these to a list containing 1) the length of the ship and 2) another list with the ships' coordinates on the board
ships = {
    "Patrol Boat": [2, []],
    "Submarine": [3, []],
    "Destroyer": [3, []],
    "Battleship": [4, []],
    "Aircraft Carrier": [5, []]
}

# Number of turns
turns = 50

# Populates initial board
for x in range(10):
    board.append(["O"] * 10)

# Prints introduction
print("Let's play Battleship!  You get %d turns." % (turns))

print_board(board)

# Calls random_ship function to populate the board with ships
for key in ships:
    random_ship(board, ships, key)

# Prints ships' coordinates for debugging purposes
# for key in ships:
# print key
# print ships[key][1]
# print " "


# This part onward is the actual guessing portion of the game, encased in a for loop that iterates for a set number of turns, or until the player wins

sunk_counter = 0

for i in range(1, turns):

    print("Turn: " + str(i))

    guess_row = int(input("Guess Row:")) - 1
    guess_col = int(input("Guess Col:")) - 1

    correct_guess = False
    hit_ship = ""

    for key in ships:
        if [guess_row, guess_col] in ships[key][1]:
            correct_guess = True
            hit_ship = key
            break

    if correct_guess == True:
        if board[guess_row][guess_col] == "*":
            print_board(board)
            print("You guessed that one already.")
        else:
            board[guess_row][guess_col] = "*"
            print_board(board)
            print("Hit!")

            hit_counter = 0

            for i in ships[hit_ship][1]:
                if board[i[0]][i[1]] == "*":
                    hit_counter += 1
            if hit_counter == ships[hit_ship][0]:
                print("Sunk " + hit_ship + "!")
                sunk_counter += 1
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col \
                                                        < 0 or guess_col > 9):
            print_board(board)
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X" or \
                        board[guess_row][guess_col] == "*":
            print_board(board)
            print("You guessed that one already.")
        else:
            board[guess_row][guess_col] = "X"
            print_board(board)
            print("Miss")

    if sunk_counter == 5:
        break

# Checks to see if you won or lost
if sunk_counter == 5:
    print("You Win!")
else:
    print("You Lose")