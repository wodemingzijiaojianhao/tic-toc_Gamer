class input_handler:
    size = 0
    def printIntro(self):
        print("Welcome to Tic Tac Toe!")
        print("You will be playing against the computer.")
        print("You can choose the size of the board.")
        print("The game will end when one player has filled a row, column, or diagonal.")
        print("The computer will always play as 'O' and you will play as 'X'.")
        print("To make a move, please enter the row and column of the position you want to fill.")
        print("The row counted from top to bottom and the column counted from left to right.")
        print("The first row and column is indexed as 1. When you make a move, please enter the position in the format of row index + column index.")
        print("For example, if you want to fill the position in the second row and first column, please enter 21.")
        print("Good luck!")
    def getSize(self):
        while True:
            try:
                size = int(input("Please enter the size of the board you want: "))
            except:
                print("Invalid input. Please enter a number.")
            if size < 2 or size > 6:
                print("Size must between 2 and 6. Please try again.")
                continue
            self.size = size
            return size
    def getNextMove(self, layoutArray): # For specialLocation, b means bottom, t means top, l means left, r means right
        while True:
            try:
                move = int(input("Please enter the move:"))
                move = move - 10 - 1 
                row = move//10
                column = move%10
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
        if playerWinning == 0:
            print("Congratulations! You win!")
        elif playerWinning == 1:
            print("Sorry, you lose. Better luck next time!")
        elif playerWinning == 2:
            print("The game is drawn.")
        ans = input("Wanna play again? (y/n)")
        if ans.lower() == 'y':
            return True
        else:
            print("Thanks for playing!")
            return False
                
