class line_detecter:
    def __init__(self, size):
        self.size = int(size)
    def detect(self, layoutArray):
        counter = 0
        consecutiveCount = 0
        previousPiece = " "
        returnArray = []
        # Check rows
        while counter < len(layoutArray):
            previousPiece = layoutArray[counter]
            counter += 1
            for i in range(self.size-1):
                if layoutArray[counter] == previousPiece and layoutArray[counter] != " ":
                    consecutiveCount += 1
                else:
                    consecutiveCount = 0
                previousPiece = layoutArray[counter]
                counter += 1
            if consecutiveCount == self.size - 1:
                for j in range(self.size):
                    returnArray.append(counter-j-1)
                return returnArray
            consecutiveCount = 0
        counter = 0
        previousPiece = " "
        # Check columns
        layoutArrayHoriz = []
        for column in range(self.size):
            for row in range(self.size):
                layoutArrayHoriz.append(layoutArray[row*self.size+column])
        while counter < len(layoutArrayHoriz):
            previousPiece = layoutArrayHoriz[counter]
            counter += 1
            for i in range(self.size-1):
                if layoutArrayHoriz[counter] == previousPiece and layoutArrayHoriz[counter] != " ":
                    consecutiveCount += 1
                else:
                    consecutiveCount = 0
                previousPiece = layoutArrayHoriz[counter]
                counter += 1
            print(counter) #test code
            print(consecutiveCount) #test code
            if consecutiveCount == self.size - 1:
                for j in range(self.size):
                    returnArray.append(((counter-j-1)%self.size)*self.size + ((counter-j-1)//self.size))
                return returnArray
            consecutiveCount = 0
        counter = 0
        previousPiece = " "
        # Check diagonals
        # Second stroke of X
        row, column = self.size - 1, 0
        previousPiece = layoutArray[row*self.size + column]
        row -= 1; column += 1
        while row >= 0 and column <= self.size-1:
            if previousPiece == layoutArray[row*self.size + column]:
                consecutiveCount += 1
            else:
                consecutiveCount = 0
            previousPiece = layoutArray[row*self.size + column]
            row -= 1; column += 1
        if consecutiveCount == self.size - 1:
            for j in range(self.size):
                returnArray.append((self.size-1-j)*self.size+j)
                return returnArray
        # First stroke of X
        consecutiveCount, previousPiece, row, column = 0, " ", 0, 0
        previousPiece = layoutArray[row*self.size + column]
        row += 1; column += 1
        while row <= self.size-1 and column <= self.size-1:
            if previousPiece == layoutArray[row*self.size + column]:
                consecutiveCount += 1
            else:
                consecutiveCount = 0
            previousPiece = layoutArray[row*self.size + column]
            row += 1; column += 1
        if consecutiveCount == self.size - 1:
            for j in range(self.size):
                returnArray.append(j*self.size+j)
                return returnArray




        
