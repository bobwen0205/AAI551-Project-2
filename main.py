# Author: Mingzhi Wen
# Date: Nov 16, 2023
# Description: This program is the start of game Captain Veggie
from GameEngine import GameEngine

def main():
    # Create an instance of the GameEngine class
    game = GameEngine()
    # Initialize the game by setting up vegetables, Captain, Rabbits, and Snake
    game.initializeGame()
    # Display the game introduction
    game.intro()
    # Get the initial count of remaining vegetables
    remaining_vegetables = game.remainingVeggies()
    # Continue the game loop until all vegetables are harvested
    while remaining_vegetables != 0:
        # Display the current game status (remaining vegetables and score)
        print(f"{remaining_vegetables} veggies remaining. Current score: {game.getScore()}")
        # Display the game field
        game.printField()
        # Move Rabbits, Captain, and Snake in the game
        game.moveCaptain()
        game.moveRabbits()
        game.moveSnake()
        # Update the count of remaining vegetables for the next iteration
        remaining_vegetables = game.remainingVeggies()
    # Display the game over message and the player's performance
    game.gameOver()
    # Display and update the high score list
    game.highScore()
# Call the main function to start the game
main()