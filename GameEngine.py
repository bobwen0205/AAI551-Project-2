# Author: Mingzhi Wen
# Date: Nov 16, 2023
# Description: This program is the GameEngine of game Captain Veggie
import os
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake
import random
import pickle

class GameEngine:
    # Constants for the game
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        # Initialize the game variables
        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__vegetables = []
        self.__score = 0
        self.__snake = None

    def initVeggies(self):
        # Prompt user for vegetable point file and initialize vegetables
        file_not_exist = True
        while file_not_exist:
            file_name = input("Please enter the name of the vegetable point file: ");
            if not os.path.exists(file_name):
                print(f"{file_name} does not exist!", end="")
            else:
                file_not_exist = False

        # Read vegetable point file and create Veggie objects
        with open(file_name, 'r') as my_file:
            line1 = my_file.readline().strip().split(',')
            rows = int(line1[1])
            cols = int(line1[2])
            self.__field = [[None for _ in range(cols)] for _ in range(rows)]
            for line in my_file:
                name = line.strip().split(',')[0]
                symbol = line.strip().split(',')[1]
                point = int(line.strip().split(',')[2])
                veggie_object = Veggie([name, symbol], point)
                self.__vegetables.append(veggie_object)
            my_file.close()

        # Distribute vegetables randomly on the field
        types_of_vegetable = len(self.__vegetables)
        nums_of_one_vegetable = []
        if self.__NUMBEROFVEGGIES > types_of_vegetable:
            split_points = sorted(random.sample(range(1, self.__NUMBEROFVEGGIES - (types_of_vegetable - 1)), types_of_vegetable - 1))
            nums_of_one_vegetable = [split_points[0]] + [split_points[i] - split_points[i - 1] for i in range(1, types_of_vegetable - 1)] + [self.__NUMBEROFVEGGIES - split_points[-1]]
        else:
            for _ in range(self.__NUMBEROFVEGGIES):
                nums_of_one_vegetable.append(1)
        for i in range(len(nums_of_one_vegetable)):
            num = nums_of_one_vegetable[i]
            for _ in range(num):
                empty_space = True
                while empty_space:
                    x = random.randrange(len(self.__field))
                    y = random.randrange(len(self.__field[0]))
                    if self.__field[x][y] is None:
                        self.__field[x][y] = self.__vegetables[i]
                        empty_space = False

    def initCaptain(self):
        # Initialize Captain on a random position in the field
        empty_space = True
        while empty_space:
            x = random.randrange(len(self.__field))
            y = random.randrange(len(self.__field[0]))
            if self.__field[x][y] is None:
                self.__captain = Captain(x, y)
                self.__field[x][y] = self.__captain
                empty_space = False

    def initRabbits(self):
        for i in range(self.__NUMBEROFRABBITS):
            empty_space = True
            while empty_space:
                x = random.randrange(len(self.__field))
                y = random.randrange(len(self.__field[0]))
                if self.__field[x][y] is None:
                    rabbit_object = Rabbit(x, y)
                    self.__rabbits.append(rabbit_object)
                    self.__field[x][y] = self.__rabbits[i]
                    empty_space = False

    def initSnake(self):
        # Initialize Snake on a random position in the field
        empty_space = True
        while empty_space:
            x = random.randrange(len(self.__field))
            y = random.randrange(len(self.__field[0]))
            if self.__field[x][y] is None:
                self.__snake = Snake(x, y)
                self.__field[x][y] = self.__snake
                empty_space = False

    def initializeGame(self):
        # Call initialization methods to set up the game
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()

    def remainingVeggies(self):
        # Count the number of remaining vegetables in the field
        nums_of_vegetables = 0
        for row in self.__field:
            for obj in row:
                if isinstance(obj, Veggie):
                    nums_of_vegetables += 1
        return nums_of_vegetables

    def intro(self):
        # Display the game introduction
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest\n"
              "as many vegetables as possible before the rabbits eat them\n"
              "all! Each vegetable is worth a different number of points\n"
              "so go for the high score!\n")
        print("The vegetables are:")
        for veggie in self.__vegetables:
            print(veggie)
        print("\nCaptain Veggie is V, and the rabbits are R's.\n")
        print("Good luck!")

    def printField(self):
        # Display the game field
        for _ in range(len(self.__field[0]) * 3 + 1):
            print('#', end="")
        print('#')
        for row in self.__field:
            print('#', end=" ")
            for i in range(len(row)):
                if i != len(row) - 1:
                    if not row[i] is None:
                        print(row[i].getSymbol(), end="  ")
                    else:
                        print(" ", end="  ")
                else:
                    if not row[i] is None:
                        print(row[i].getSymbol(), end=" ")
                    else:
                        print(" ", end=" ")
            print('#')
        for _ in range(len(self.__field[0]) * 3 + 1):
            print('#', end="")
        print('#')

    def getScore(self):
        # Return the player's current score
        return self.__score

    def moveRabbits(self):
        # Move Rabbit objects randomly on the field
        delta_x = [0, -1, 1, 0, 0, -1, -1, 1, 1]
        delta_y = [0, 0, 0, -1, 1, -1, 1, -1, 1]
        for rabbit in self.__rabbits:
            # 0 for no move, 1 for up, 2 for down, 3 for left, 4 for right
            # 5 for up-left, 6 for up-right, 7 for down-left, 8 for down-right
            direction = random.randint(0, 8)
            x = rabbit.get_coordinate()[0]
            y = rabbit.get_coordinate()[1]
            new_x = x + delta_x[direction]
            new_y = y + delta_y[direction]
            if direction == 0:
                continue
            else:
                if new_x < 0 or new_x >= len(self.__field) or new_y < 0 or new_y >= len(self.__field[0]):
                    continue
                elif isinstance(self.__field[new_x][new_y], Rabbit) or isinstance(self.__field[new_x][new_y], Captain):
                    continue
                elif isinstance(self.__field[new_x][new_y], Veggie):
                    self.__field[new_x][new_y] = rabbit
                    rabbit.set_new_xy(new_x, new_y)
                    self.__field[x][y] = None
                else:
                    self.__field[new_x][new_y] = rabbit
                    rabbit.set_new_xy(new_x, new_y)
                    self.__field[x][y] = None

    def moveCptVertical(self, direction):
        # Move Captain vertically based on user input
        x = self.__captain.get_coordinate()[0]
        y = self.__captain.get_coordinate()[1]
        if direction == 'W' or direction == 'w':
            new_x = x - 1
        elif direction == 'S' or direction == 's':
            new_x = x + 1
        if self.__field[new_x][y] is None:
            self.__field[new_x][y] = self.__captain
            self.__captain.set_new_xy(new_x, y)
            self.__field[x][y] = None
        elif isinstance(self.__field[new_x][y], Veggie):
            self.__captain.addVeggie(self.__field[new_x][y])
            print(f"Yummy! A delicious {self.__field[new_x][y].getName()}")
            self.__score += self.__field[new_x][y].getPoints()
            self.__field[new_x][y] = self.__captain
            self.__captain.set_new_xy(new_x, y)
            self.__field[x][y] = None
        elif isinstance(self.__field[new_x][y], Rabbit):
            print("Don't step on the bunnies!")

    def moveCptHorizontal(self, direction):
        # Move Captain horizontally based on user input
        x = self.__captain.get_coordinate()[0]
        y = self.__captain.get_coordinate()[1]
        if direction == 'A' or direction == 'a':
            new_y = y - 1
        elif direction == 'D' or direction == 'd':
            new_y = y + 1
        if self.__field[x][new_y] is None:
            self.__field[x][new_y] = self.__captain
            self.__captain.set_new_xy(x, new_y)
            self.__field[x][y] = None
        elif isinstance(self.__field[x][new_y], Veggie):
            self.__captain.addVeggie(self.__field[x][new_y])
            print(f"Yummy! A delicious {self.__field[x][new_y].getName()}")
            self.__score += self.__field[x][new_y].getPoints()
            self.__field[x][new_y] = self.__captain
            self.__captain.set_new_xy(x, new_y)
            self.__field[x][y] = None
        elif isinstance(self.__field[x][new_y], Rabbit):
            print("Don't step on the bunnies!")

    def moveCaptain(self):
        # Move the Captain based on user input
        x = self.__captain.get_coordinate()[0]
        y = self.__captain.get_coordinate()[1]
        direction = input("Would you like to move up(W), down(S), left(A), or right(D):")
        if direction == 'W' or direction == 'w':
            if x - 1 >= 0:
                self.moveCptVertical(direction)
            else:
                print("You can't move that way!")
        elif direction == 'S' or direction == 's':
            if x + 1 < len(self.__field):
                self.moveCptVertical(direction)
            else:
                print("You can't move that way!")
        elif direction == 'A' or direction == 'a':
            if y - 1 >= 0:
                self.moveCptHorizontal(direction)
            else:
                print("You can't move that way!")
        elif direction == 'D' or direction == 'd':
            if y + 1 < len(self.__field[0]):
                self.moveCptHorizontal(direction)
            else:
                print("You can't move that way!")
        else:
            print(f"{direction} is not a valid option")

    def moveSnake(self):
        # Move the Snake toward the Captain
        captain_x = self.__captain.get_coordinate()[0]
        captain_y = self.__captain.get_coordinate()[1]
        snake_x = self.__snake.get_coordinate()[0]
        snake_y = self.__snake.get_coordinate()[1]
        # Which direction should snake move to attack captain
        vertical = snake_x - captain_x
        horizontal = snake_y - captain_y
        new_snake_x = snake_x
        new_snake_y = snake_y
        # If vertical distance is greater than horizontal distance
        # The snake move vertically
        if abs(vertical) > abs(horizontal):
            if vertical > 0:
                new_snake_x = snake_x - 1
            else:
                new_snake_x = snake_x + 1
        # If vertical distance is less than horizontal distance
        # The snake move horizontally
        else:
            if horizontal > 0:
                new_snake_y = snake_y - 1
            else:
                new_snake_y = snake_y + 1
        if 0 <= new_snake_x < len(self.__field) and 0 <= new_snake_y < len(self.__field[0]):
            times = 0
            while isinstance(self.__field[new_snake_x][new_snake_y], Rabbit) or isinstance(self.__field[new_snake_x][new_snake_y], Veggie):
                times += 1
                # Vertical move meet rabbit or veggie so move horizontally
                if abs(new_snake_x - snake_x) == 1:
                    new_snake_x = snake_x
                    if horizontal > 0 and 0 <= snake_y - 1 < len(self.__field[0]):
                        new_snake_y = snake_y - 1
                    elif horizontal <= 0 and 0 <= snake_y + 1 < len(self.__field[0]):
                        new_snake_y = snake_y + 1
                # Horizontal move meet rabbit or veggie so move vertically
                elif abs(new_snake_y - snake_y) == 1:
                    new_snake_y = snake_y
                    if vertical > 0 and 0 <= snake_x - 1 < len(self.__field):
                        new_snake_x = snake_x - 1
                    elif vertical <= 0 and 0 <= snake_x + 1 < len(self.__field):
                        new_snake_x = snake_x + 1
                if times == 4:
                    break
            if isinstance(self.__field[new_snake_x][new_snake_y], Captain):
                print("Oops! A snake attacked you, you lose the last 5 vegetables!")
                for _ in range(5):
                    if len(self.__captain.get_collection_list()) != 0:
                        self.__captain._collection_list.pop()
                self.__field[snake_x][snake_y] = None
                self.__snake = None
                self.initSnake()
            elif self.__field[new_snake_x][new_snake_y] is None:
                self.__field[new_snake_x][new_snake_y] = self.__snake
                self.__snake.set_new_xy(new_snake_x, new_snake_y)
                self.__field[snake_x][snake_y] = None

    def gameOver(self):
        # Display game over message and player's performance
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for vegetable in self.__captain.get_collection_list():
            print(vegetable.getName())
        print(f"Your score was: {self.__score}")

    def highScore(self):
        # Display and update the high score list
        high_score_list = []
        if os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, 'rb') as myFile:
                high_score_list = pickle.load(myFile)
                myFile.close()
        initial = input("Please enter your three initials to go on the scoreboard: ")
        initial = initial.strip().upper()[0: 3]
        if len(high_score_list) == 0:
            initial_score_tuple = (initial, self.__score)
            high_score_list.append(initial_score_tuple)
        else:
            for i in range(len(high_score_list)):
                score = high_score_list[i][1]
                if self.__score > score:
                    high_score_list.insert(i, (initial, self.__score))
                    break
                if i == len(high_score_list) - 1:
                    high_score_list.append((initial, self.__score))
        print("HIGH SCORES")
        print("Name\t\t\tScore")
        for initial_score in high_score_list:
            print(f"{initial_score[0]}\t\t\t\t{initial_score[1]}")
        with open(self.__HIGHSCOREFILE, 'wb') as myFile:
            pickle.dump(high_score_list, myFile)
            myFile.close()

