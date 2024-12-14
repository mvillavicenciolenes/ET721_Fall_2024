# Description

# 1.	Class Connect4:
# 	•	This class manages the entire Connect4 game logic. It contains methods for switching players,       displaying the board, dropping a chip in a column, checking for a win, and running the main game loop.
# 	
# 2.	__init__ Method:
# 	•	Initializes the game board as a 6x7 grid with empty spaces, stored in self.board. Sets self.current_player to ‘X’ to signify that player X goes first.
# 	
# 3.	switch_player Method:
# 	•	Toggles self.current_player between ‘X’ and ‘O’ after each turn.
# 	
# 4.	print_board Method:
# 	•	Outputs the current state of the board in a visual format for easy viewing. Adds row and column markers to guide player choices.
# 	
# 5.	drop_chip Method:
# 	•	Allows the player to add a chip to a chosen column, checking from the bottom-most row up for an empty slot. It returns False if the column is out of range or full.
# 	
# 6.	check_win Method:
# 	•	Detects if the current player has four consecutive chips in a row, column, or diagonal. Returns True if the player wins, otherwise False.
# 	
# 7.	play_game Method:
# 	•	Executes the game loop, prompting the player for a column choice, dropping a chip, checking for a win, and switching players until there’s a winner or the board fills up.

# Suggested Changes and Observations

# 	1.	Board Size:
# 	•	Change: Modify self.board = [[' ' for _ in range(7)] for _ in range(6)] to use different dimensions, like a 5x5 grid.
# 	•	Observation: A smaller or larger board size would significantly alter the game’s difficulty and play length. 
#       A smaller board might lead to quicker games and more frequent wins, while a larger board would require more strategy and potentially longer play sessions.

# 	2.	Switching Players (switch_player):
# 	•	Change: Add an option to let players choose who goes first or allow the computer to select a random starting player.
# 	•	Observation: Adjusting the starting player or making it random can add variety and fairness in repeated games. Players may experience a more balanced gameplay flow.

# 	3.	Win Condition (check_win):
# 	•	Change: Modify the win condition to require a different number of consecutive chips (e.g., three or five).
# 	•	Observation: Changing the consecutive count required to win would affect the game’s strategy. Lowering it to three makes it easier to win, increasing the pace. 
#       Raising it makes the game more challenging, especially on     larger boards.

# 	4.	Input Validation in drop_chip:
# 	•	Change: Add more detailed messages for invalid inputs, such as out-of-range entries and full columns.
# 	•	Observation: This enhancement would improve user experience by making errors clearer and helping players correct mistakes without frustration.

# 	5.	End of Game (play_game method):
# 	•	Change: Add functionality to detect a draw when all columns are full without any player winning.
# 	•	Observation: Without a draw condition, the game could continue indefinitely if players fail to align four in a row. Including this feature would give closure to games where a win is impossible.

# 	6.	Alternate Winning Conditions:
# 	•	Change: Implement “complex win” conditions, such as requiring a diagonal and a row simultaneously.
# 	•	Observation: This modification would make the game more challenging and would encourage players to think several moves ahead, adding a level of depth.

# 	7.	AI Player Option:
# 	•	Change: Develop an AI-based method to make moves when only one player is present.
# 	•	Observation: Adding an AI player would enhance the game’s functionality and make it enjoyable for solo play, especially with AI strategies that range from beginner to advanced.