# Connect 4 Game

class Connect4:
    # Initialize the game board and set the starting player
    def __init__(self):
        # Create a 6x7 grid filled with spaces (' ') to represent an empty board
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        # Set the current player to 'X' as the starting player
        self.current_player = 'X'

    # Function to switch to the other player
    def switch_player(self):
        # Changes the current player from 'X' to 'O' or vice versa
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    # Function to print the current state of the board
    def print_board(self):
        # Iterate over each row to print the board structure
        for row in self.board:
            print('|', end='')  # Start each row with a '|'
            for cell in row:
                print(cell, end='|')  # Print each cell with a '|' boundary
            print()  # Move to the next line after each row
        print('---------------')  # Print a line separator below the board
        print(' 1 2 3 4 5 6 7')  # Display column numbers for user reference

    # Function to drop a chip in the specified column
    def drop_chip(self, column):
        """
        Drops the current player's chip in the specified column.

        Args:
          column (int): Column number (1-7) for the chip to be dropped.

        Returns:
          bool: True if the chip was successfully placed, False if the column is full or out of range.
        """
        # Check if the column is within the valid range (1-7)
        if column < 1 or column > 7:
            return False

        # Start from the bottom row and find the first empty slot in the specified column
        row = 5  # Start checking from the bottom of the column
        while row >= 0:
            # If an empty slot is found, break out of the loop
            if self.board[row][column - 1] == ' ':
                break
            row -= 1  # Move one row up if the slot is not empty

        # If no empty slot was found, return False (column is full)
        if row < 0:
            return False

        # Place the current player's chip in the found slot
        self.board[row][column - 1] = self.current_player
        return True  # Return True to indicate successful placement

    # Function to check if the current player has won the game
    def check_win(self, player):
        """
        Checks if the specified player has four consecutive chips in a row.

        Args:
          player (str): The player ('X' or 'O') to check for a win.

        Returns:
          bool: True if the player has won, otherwise False.
        """
        # Check for horizontal win
        for row in range(6):
            for col in range(4):  # Only check columns where a 4-in-a-row is possible
                if (self.board[row][col] == player and
                    self.board[row][col + 1] == player and
                    self.board[row][col + 2] == player and
                    self.board[row][col + 3] == player):
                    return True  # Player wins with horizontal alignment

        # Check for vertical win
        for row in range(3):  # Only check rows where a 4-in-a-row is possible
            for col in range(7):
                if (self.board[row][col] == player and
                    self.board[row + 1][col] == player and
                    self.board[row + 2][col] == player and
                    self.board[row + 3][col] == player):
                    return True  # Player wins with vertical alignment

        # Check for diagonal win (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == player and
                    self.board[row + 1][col + 1] == player and
                    self.board[row + 2][col + 2] == player and
                    self.board[row + 3][col + 3] == player):
                    return True  # Player wins with diagonal (↘) alignment

        # Check for diagonal win (bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if (self.board[row][col] == player and
                    self.board[row - 1][col + 1] == player and
                    self.board[row - 2][col + 2] == player and
                    self.board[row - 3][col + 3] == player):
                    return True  # Player wins with diagonal (↗) alignment

        return False  # No win found, return False

    # Main function to start and control the game flow
    def play_game(self):
        game_over = False  # Flag to track if the game has ended
        while not game_over:
            # Print the current board state and prompt player action
            self.print_board()
            print(f"Player {self.current_player}'s turn.")

            # Get the column input from the player
            try:
                column = int(input("Enter the column number (1-7): "))
            except ValueError:
                # Error message if input is not a valid number
                print("Invalid input. Please enter a valid column number.")
                continue

            # Attempt to drop the chip in the specified column
            if not self.drop_chip(column):
                # Error message if the column is full or out of range
                print("Column is full or out of range. Try again.")
                continue

            # Check if the current player has won after their move
            if self.check_win(self.current_player):
                # Print the board and announce the winner
                self.print_board()
                print(f"Player {self.current_player} wins!")
                game_over = True  # End the game
            else:
                # Switch to the other player if the game continues
                self.switch_player()

# Execute the game if this file is run directly
if __name__ == "__main__":
    game = Connect4()  # Create an instance of the Connect4 class
    game.play_game()  # Start the game
'''
Explanation Summary:

	1.	Class Initialization (__init__): Sets up an empty board and starts the game with player 'X'.
	2.	Switch Player (switch_player): Alternates the current player from 'X' to 'O' after each turn.
	3.	Print Board (print_board): Displays the current state of the game board for players.
	4.	Drop Chip (drop_chip): Places a chip in the specified column, finding the next available slot from the bottom. Returns True if the move is successful and False if the column is full or invalid.
	5.	Check Win (check_win): Checks for a win by identifying four consecutive chips for the current player in horizontal, vertical, or diagonal directions.
	6.	Play Game (play_game): Manages game flow, prompting players to take turns until one wins or an error message is printed if an invalid move is made.

This setup creates a loop that continuously alternates between players, updating the board and checking for wins after each move. The functions are closely connected, so changing any part (like board dimensions) would require updating multiple parts of the code to keep it consistent.
'''