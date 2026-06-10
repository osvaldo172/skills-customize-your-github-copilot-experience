
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman game in Python that uses user input, string handling, loops, and conditionals to let a player guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Hangman Game

#### Description

Create a Hangman game that randomly selects a word from a list and lets the player guess letters until they either reveal the word or use all allowed attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list
- Ask the player to guess a single letter at a time
- Show the current word progress with blanks and correctly guessed letters, like `_ a _ g _ a _`
- Keep track of letters already guessed and prevent duplicate processing
- Count incorrect guesses and display remaining attempts
- End with a clear win message if the word is guessed or a lose message if attempts run out

### 🛠️ Gameplay Improvements

#### Description

Make the game more user-friendly by handling invalid input and allowing the player to keep playing until the game is complete.

#### Requirements
Completed program should:

- Ignore invalid guesses like empty input or non-letter characters
- Inform the player when a letter has already been guessed
- Display the current guessed letters and remaining attempts after each turn
- Optionally allow the player to play again after a finished game
