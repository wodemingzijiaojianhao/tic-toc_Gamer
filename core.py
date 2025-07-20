class core:
    def __init__(self):
        self.size = -1
        self.layoutArray = [" " for _ in range(self.size * self.size)]
    def initCommandLineGame(self):
        import output_handler as oh
        import input_handler as ih
        self.ih.printIntro()
        self.size = self.ih.getSize()
        self.coh = oh(self.size)
        self.cih = ih()
        gameEnd = False
        self.coh.printOut()
        while not gameEnd:
            row, column = self.cih.getNextMove(self, self.layoutArray)
            self.layoutArray[(row*self.size)+column] = "O"
            self.coh.update(row, column, "O")
            self.coh.printOut()
    def calcNextMove(self, layoutArray):
        import line_detecter as ld
        self.cld = ld(self.size)
        highestScore = -10000
        highestIndex = -1
        for i in range(len(layoutArray)):
            if layoutArray[i] == " ":
                layoutArray[i] = "O"
                score, flag = self.calcScore(layoutArray, "O", self.cld, self.size*self.size)
                layoutArray[i] = " "
                if flag == 1:
                    return i // self.size, i % self.size, True # This boolean indicate whether the computer wins for the next step
                if score > highestScore:
                    highestScore = score
                    highestIndex = i
        if highestIndex != -1:
            row = highestIndex // self.size
            column = highestIndex % self.size
            return row, column, False
        else:
            return -1, -1, False  #This indicate the game is drawn
    def calcScore(self, layoutArray, piece, lineDetecter, weight):
        detection = lineDetecter.detect(layoutArray)
        if len(detection) != 0:
            if layoutArray[detection[0]] == "X":
                return -1*weight, 0   #The second argument indicates if game win/lost on the current move
            elif layoutArray[detection[0]] == "O":
                return 1*weight, 1
        else:
            scores = []
            if piece == "O":
                for i in range(len(layoutArray)):
                    if layoutArray[i] == " ":
                        layoutArray[i] = "X"
                        scores.append(self.calcScore(layoutArray, "X", lineDetecter, weight-1)[0])
                        layoutArray[i] = " "
                if len(scores) == 0:
                    return 0, 2
                else:
                    return min(scores), 3
            elif piece == "X":
                for i in range(len(layoutArray)):
                    if layoutArray[i] == " ":
                        layoutArray[i] = "O"
                        scores.append(self.calcScore(layoutArray, "O", lineDetecter, weight-1)[0])
                        layoutArray[i] = " "
                if len(scores) == 0:
                    return 0, 4
                else:
                    return max(scores), 5

