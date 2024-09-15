# Higher-Lower Game 📊

A console-based guessing game implemented in Python, where players compare the follower counts of two random entries and try to guess which one has more followers.

## Features

- **Random Data**: Retrieves random entries from a dataset and displays their details.
- **User Interaction**: Players guess which entry has more followers by typing 'A' or 'B'.
- **Score Tracking**: Tracks the player's score based on correct guesses.
- **Game End**: The game continues until the player makes an incorrect guess, displaying the final score.

## How It Works

1. **Initialization**: The game displays a welcome message and logo.
2. **Game Loop**:
    - Randomly selects two entries from the dataset.
    - Shows details of both entries.
    - Prompts the player to guess which entry has more followers.
    - Compares the follower counts and updates the score based on the player's guess.
    - Ends the game if the player guesses incorrectly and displays the final score.

## Code Overview

- **`clear()`**: Clears the console screen by printing new lines.
- **`a_greater_than_b(a_dict, b_dict)`**: Compares the follower counts of two dictionary entries.
- **`start()`**: Main function to run the game loop, handle user input, and display results.

## Dependencies

- `art`: Contains game logo and other ASCII art.
- `game_data`: Provides the dataset of entries to be compared.
- `random`: Used to select random entries from the dataset.
- 

## Future Improvements

- Add a graphical user interface (GUI) for a more interactive experience.
- Expand the dataset with more diverse entries.
- Implement a high score feature to track top scores.


