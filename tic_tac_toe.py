
# TIC-TAC-TOE
# Lab 05

# 1. Create a 3x3 game board
matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# 2. Store the players
players = ["O", "X"]

# 3. Count the number of valid turns
turns = 0

# 4. Store the winner
winner = None


# Function to display the game board
def display_board():
    for row in matrix:
        for column_index, cell in enumerate(row):
            if column_index > 0:
                print("|", end=" ")
            print(cell, end=" ")
        print()


# Function to check whether a player has won
def check_winner(player):
    # Check horizontal rows
    for row_index, row in enumerate(matrix):
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check vertical columns
    for column in range(3):
        if (
            matrix[0][column] == player
            and matrix[1][column] == player
            and matrix[2][column] == player
        ):
            return True

    # Check the diagonal from top-left to bottom-right
    if (
        matrix[0][0] == player
        and matrix[1][1] == player
        and matrix[2][2] == player
    ):
        return True

    # Check the diagonal from top-right to bottom-left
    if (
        matrix[0][2] == player
        and matrix[1][1] == player
        and matrix[2][0] == player
    ):
        return True

    return False


# 5. Main game loop
while turns < 9 and winner is None:

    # Select X first, then alternate with O
    current_player = players[(turns + 1) % 2]

    print("\nTIC-TAC-TOE")
    display_board()
    print(f"\n{current_player}'s Turn")

    # 6. Get and validate the player's move
    try:
        row = int(input("Enter row (1-3): "))
        column = int(input("Enter column (1-3): "))
    except ValueError:
        print("Invalid input! Please enter numbers from 1 to 3.")
        continue

    # Check that the row and column are within the board
    if row not in range(1, 4) or column not in range(1, 4):
        print("Invalid row or column! Please enter numbers from 1 to 3.")
        continue

    # Convert user input to Python list indexes
    row_index = row - 1
    column_index = column - 1

    # Check whether the selected space is occupied
    if matrix[row_index][column_index] != "-":
        print(f"Someone has already claimed {row}:{column}!")
        input("Hit [enter] to continue.")
        continue

    # Place the player's marker
    matrix[row_index][column_index] = current_player

    # Check whether the current player has won
    if check_winner(current_player):
        winner = current_player

    # Count the valid move
    turns += 1


# 7. Game over
print("\nTIC-TAC-TOE")
display_board()

if winner is not None:
    print(f"\n{winner} won!")
elif turns == 9:
    print("\nIt's a draw!")

print("Game Over!")
print("Thanks for playing!")
