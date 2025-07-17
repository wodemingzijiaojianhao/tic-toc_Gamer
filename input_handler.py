class input_handler:
    size = 0
    def printIntro(self):
        print("Welcome to Tic Tac Toe!")
        print("You will be playing against the computer.")
        print("You can choose the size of the board.")
        print("The game will end when one player has filled a row, column, or diagonal.")
        print("Good luck!")
    def getSize(self):
        while True:
            try:
                size = int(input("Please enter the size of the board: "))
            except:
                print("Invalid input. Please enter a number.")
            if size < 3 or size > 6:
                print("Size must between 3 and 6. Please try again.")
                continue
            self.size = size
            return size
    def getNextMove(self, layoutArray): # For specialLocation, b means bottom, t means top, l means left, r means right
        while True:
            try:
                move = int(input("Enter the next move:"))
                move = move - 10 - 1 
                row = move//10
                column = move%10
                print(row, column) #test code
                if self.checkPositionValidity(layoutArray, row, column):
                    return row, column
                else:
                    print("This position is already taken, please try again.")
                    continue
            except Exception as e:
                print("Invalid input. Please follow the instructions stated in the game introduction.")

    def checkPositionValidity(self, layoutArray, row, column):
        if layoutArray[row*self.size+column] != " ":
            return False
        else:
            return True
    def announceWinner(self, playerWinning): # playerWinning is a boolean indicate whether the player wins
        if playerWinning:
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Better luck next time!")
        ans = input("Wanna play again? (y/n)")
        if ans.lower() == 'y':
            return True
        else:
            print("Thanks for playing!")
            return False
                
