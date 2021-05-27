def checkIfDigit(value):
    if value.isdigit():  # Checks if the value provided is a number, we are going to use this for input validation

        return True

    else:
        return False


class TicTacToe:
    def __init__(self):
        self.player1 = "X"
        self.player2 = "O"

        self.board = {'1': " ", '2': " ", '3': " ",
                      '4': " ", '5': " ", '6': " ",
                      '7': " ", '8': " ", '9': " "}

    def showIntro(self):
        print(''' 
             _    _      _                            _____       _____ _            _____ _        _____            _____            _____                        _ 
            | |  | |    | |                          |_   _|     |_   _| |          |_   _(_)      |_   _|          |_   _|          |  __ \                      | |
            | |  | | ___| | ___ ___  _ __ ___   ___    | | ___     | | | |__   ___    | |  _  ___    | | __ _  ___    | | ___   ___  | |  \/ __ _ _ __ ___   ___  | |
            | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \    | | | '_ \ / _ \   | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \ | | __ / _` | '_ ` _ \ / _ \ | |
            \  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |   | | | | | |  __/   | | | | (__    | | (_| | (__    | | (_) |  __/ | |_\ \ (_| | | | | | |  __/ |_|
             \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/    \_/ |_| |_|\___|   \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|  \____/\__,_|_| |_| |_|\___| (_)
                                                                                                                                                                     
            '''
              )

        print(f"Player 1 is {self.player1}, and Player 2 is {self.player2}\n")
        print('''To select where you want to move just type in the number of the position. The Board is like this: 
                    
                    These are the positions
         |  |    [1, 2, 3] 
        --+-+-   
         |  |    [4, 5, 6]
        --+-+-
         |  |    [7, 8, 9]
        
        ''')

    def showBoard(self):
        print(self.board["1"] + "|" + self.board['2'] + "|" + self.board['3'])
        print('-+-+-')
        print(self.board["4"] + "|" + self.board['5'] + "|" + self.board['6'])
        print('-+-+-')
        print(self.board["7"] + "|" + self.board['8'] + "|" + self.board['9'] + "\n")

    def startGame(self):
        self.showIntro()
        keepGoing = True
        gameCount = 0

        while keepGoing:
            self.playerChoice("1")
            self.showBoard()
            gameCount += 1

            if self.__checkForWinner():
                keepGoing = False
                self.showBoard()
                break

            if gameCount == 9:
                print("\nIt's a tie!")
                self.showBoard()
                keepGoing = False
                break

            self.playerChoice("2")
            self.showBoard()
            gameCount += 1

            if self.__checkForWinner():
                keepGoing = False
                self.showBoard()
                break

            if gameCount == 9:
                print("\nIt's a tie!")
                self.showBoard()
                keepGoing = False
                break

        self.__restartGame()

    def playerChoice(self, player):

        if player == "1":
            playerChoice = input(f"Player {player} turn '{self.player1}'. Where do you want to place your {self.player1}? (type in the number): ")
            self.__checkPlayerInput(player, playerChoice)

        if player == "2":
            playerChoice = input(f"Player {player} turn '{self.player2}'. Where do you want to place your {self.player2}? (type in the number): ")
            self.__checkPlayerInput(player, playerChoice)

    def __checkPlayerInput(self, player, playerInput):  # This private function is just for input validation, checks whether the value that the user provided is a number
                                                        # and if the number is between 1 and 9 because those are the positions of the board. Those numbers are the keys.

        playerOldChoice = playerInput

        if player == "1":

            if checkIfDigit(playerInput):
                if 1 <= int(playerInput) <= 9:

                    if self.board[playerInput] == "O" or self.board[playerInput] == "X":
                        print("This position is already selected, try another position.\n")
                        playerInput = input(f"Player {player} turn '{self.player1}'. Where do you want to place your {self.player1}? (type in the number): ")

                        while playerInput == playerOldChoice:
                            print("You selected the same position. Try again.\n")
                            playerInput = input(f"Player {player} turn '{self.player1}'. Where do you want to place your {self.player1}? (type in the number): ")
                        self.board[playerInput] = self.player1

                    else:
                        self.board[playerInput] = self.player1

                else:
                    while not 1 <= int(playerInput) <= 9:
                        print("Error, you should only type in numbers from 1 to 9 because those are the positions.\n")
                        playerInput = input(f"Player {player} turn '{self.player1}'. Where do you want to place your {self.player1}? (type in the number): ")
                    self.board[playerInput] = self.player1

            else:
                while not playerInput.isdigit():  # First check if the input that the user gives us is a number.
                    print("Error, you should only type in numbers from 1 to 9 because those are the positions.\n")
                    playerInput = input(f"Player {player} turn '{self.player1}'. Where do you want to place your {self.player1}? (type in the number): ")

                if checkIfDigit(playerInput):
                    if 1 <= int(playerInput) <= 9:

                        if self.board[playerInput] == "O" or self.board[playerInput] == "X":
                            print("This position is already selected, try another position.\n")
                            playerInput = input(f"Player {player} turn '{self.player1}'. Where do you want to place your {self.player1}? (type in the number): ")

                            while playerInput == playerOldChoice:
                                print("You selected the same position. Try again.\n")
                                playerInput = input(f"Player {player} turn '{self.player1}'. Where do you want to place your {self.player1}? (type in the number): ")
                            self.board[playerInput] = self.player1

                        else:
                            self.board[playerInput] = self.player1

        elif player == "2":
            if checkIfDigit(playerInput):
                if 1 <= int(playerInput) <= 9:

                    if self.board[playerInput] == "O" or self.board[playerInput] == "X":
                        print("This position is already selected, try another position.\n")
                        playerInput = input(f"Player {player} turn '{self.player2}'. Where do you want to place your {self.player2}? (type in the number): ")

                        while playerInput == playerOldChoice:
                            print("You selected the same position. Try again.\n")
                            playerInput = input(f"Player {player} turn '{self.player2}'. Where do you want to place your {self.player2}? (type in the number): ")
                        self.board[playerInput] = self.player2

                    else:
                        self.board[playerInput] = self.player2

                else:
                    while not 1 <= int(playerInput) <= 9:
                        print("Error, you should only type in numbers from 1 to 9 because those are the positions.\n")
                        playerInput = input(f"Player {player} turn '{self.player2}'. Where do you want to place your {self.player2}? (type in the number): ")
                    self.board[playerInput] = self.player2
            else:
                while not playerInput.isdigit():  # First check if the input that the user gives us is a number.
                    print("Error, you should only type in numbers from 1 to 9 because those are the positions.\n")
                    playerInput = input(f"Player {player} turn '{self.player2}'. Where do you want to place your {self.player2}? (type in the number): ")

                if checkIfDigit(playerInput):
                    if 1 <= int(playerInput) <= 9:

                        if self.board[playerInput] == "O" or self.board[playerInput] == "X":
                            print("This position is already selected, try another position.\n")
                            playerInput = input(f"Player {player} turn '{self.player2}'. Where do you want to place your {self.player2}? (type in the number): ")

                            while playerInput == playerOldChoice:
                                print("You selected the same position. Try again.\n")
                                playerInput = input(f"Player {player} turn '{self.player2}'. Where do you want to place your {self.player2}? (type in the number): ")
                            self.board[playerInput] = self.player2

                        else:
                            # self.player2Pos += playerChoice
                            self.board[playerInput] = self.player2

    def __checkForWinner(self):  # This private function checks who won by checking each value of the keys
        if self.board["1"] == self.board["2"] == self.board["3"] != " ":
            if self.board["1"] == self.board["2"] == self.board["3"] == "X":
                print("\nPlayer 1 Won!")
                return True
            else:
                print("\nPlayer 2 Won!")
                return True

        elif self.board["1"] == self.board["5"] == self.board["9"] != " ":

            if self.board["1"] == self.board["5"] == self.board["9"] == "X":
                print("\nPlayer 1 Won!")
                return True

            else:
                print("\nPlayer 2 Won!")
                return True

        elif self.board["1"] == self.board["4"] == self.board["7"] != " ":
            if self.board["1"] == self.board["4"] == self.board["7"] == "X":
                print("\nPlayer 1 Won!")
                return True
            else:
                print("\nPlayer 2 Won!")
                return True

        elif self.board["4"] == self.board["5"] == self.board["6"] != " ":
            if self.board["4"] == self.board["5"] == self.board["6"] == "X":
                print("\nPlayer 1 Won!")
                return True
            else:
                print("\nPlayer 2 Won!")
                return True

        elif self.board["7"] == self.board["8"] == self.board["9"] != " ":
            if self.board["7"] == self.board["8"] == self.board["9"] == "X":
                print("\nPlayer 1 Won!")
                return True
            else:
                print("\nPlayer 2 Won!")
                return True

        elif self.board["2"] == self.board["5"] == self.board["8"] != " ":
            if self.board["2"] == self.board["5"] == self.board["8"] == "X":
                print("\nPlayer 1 Won!")
                return True
            else:
                print("\nPlayer 2 Won!")
                return True

        elif self.board["3"] == self.board["6"] == self.board["9"] != " ":
            if self.board["3"] == self.board["6"] == self.board["9"] == "X":
                print("\nPlayer 1 Won!")
                return True
            else:
                print("\nPlayer 2 Won!")
                return True

        elif self.board["3"] == self.board["5"] == self.board["7"] != " ":
            if self.board["3"] == self.board["5"] == self.board["7"] == "X":
                print("\nPlayer 1 Won!")
                return True
            else:
                print("\nPlayer 2 Won!")
                return True

    def __restartGame(self):

        playAgain = input("\nDo you want to play again? (Y/N): ").lower()

        while playAgain != "y" and playAgain != "n":
            playAgain = input("Error. Type only 'Y' or 'N': ").lower()

        if playAgain == "y":

            self.board = {'1': " ", '2': " ", '3': " ",
                          '4': " ", '5': " ", '6': " ",
                          '7': " ", '8': " ", '9': " "}

            self.startGame()

        else:
            print("Thank you for playing! Goodbye. ")
