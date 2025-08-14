"""import output_handler as oh
import line_detecter as ld
import input_handler as ih
a = oh.output_handler(4)
b = ld.line_detecter(4)
c = ih.input_handler()

a.update(0, 2, "X")
a.update(0, 0, "O")
a.update(0, 1, "O")
a.update(0, 3, " ")
a.update(1, 1, "X")
a.update(1, 3, "X")
a.update(3, 3, "O")
a.update(3, 2, "X")
a.update(3, 1, "X")
a.update(3, 0, "X")
a.update(1, 0, "X")
a.printOut()
c.printIntro()
size = c.getSize()
for i in range (10):
    r, s = c.getNextMove(a.layoutArray)
    a.update(r, s, "O")
    a.printOut()
"""
import core as c
testGame = c.core()
testGame.initCommandLineGame()
# End of testing codes
# This is the main entry point for the Tic Tac Toe game.
# Need to put into more feature to build GUI version
# And more testing as well


