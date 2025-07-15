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
                if layoutArray[counter] == previousPiece:
                    consecutiveCount += 1
                else:
                    consecutiveCount = 0
            print(counter) #test code
            print(consecutiveCount) #test code
            if consecutiveCount == self.size - 1:
                for j in range(self.size):
                    returnArray.append(counter-j)
                return returnArray
            counter += 1
        
