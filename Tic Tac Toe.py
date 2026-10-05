

matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Create a variable to store a list of the players O and X.

players = ["O", "X"]

# 3. Create a variable to store the number of turns taken.
turns = 0


# Create a variable to store the winner of the game. Initialize it to None.
winner = None


#  Create a while loop to act as the main game loop.
while not winner and turns < 9:
    turns = turns % 2