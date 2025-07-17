class output_handler:
    def __init__(self, size):
        self.size = int(size)
        self.layoutArray = []
        for i in range(self.size*self.size):
            self.layoutArray.append(" ")
    def update(self, row, column, piece): #Piece must be O or X and in type string
        self.layoutArray[(row*self.size)+column] = piece

    def printOut(self):
        for i in range(self.size+2):
            print("- ", end='')
        print()
        for i in range(self.size):
            print("| ", end='')
            for j in range(self.size):
                print(self.layoutArray[(i*self.size)+j], end='')
                print(" ", end='')
            print("|")
        for i in range(self.size+2):
            print("- ", end='')
        print()
    def showWinner(self, winner):
        if winner == "X":
            for i in range(len(self.layoutArray)):
                if self.layoutArray[i] == "X":
                    self.layoutArray[i] = "*"
        if winner == "O":
            for i in range(len(self.layoutArray)):
                if self.layoutArray[i] == "O":
                    self.layoutArray[i] = "*"
        self.printOut()
    def highlightFromIndexArr(self, arr):
        for item in arr:
            self.layoutArray[item] = "*"
        self.printOut()
    def clear(self):
        for i in range(len(self.layoutArray)):
            self.layoutArray[i] = " "
        