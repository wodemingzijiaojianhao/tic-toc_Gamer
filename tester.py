import output_handler as oh
import line_detecter as ld
a = oh.output_handler(4)
b = ld.line_detecter(4)
a.update(0, 2, "X")
a.update(0, 0, "X")
a.update(0, 1, "O")
a.update(0, 3, "O")
a.update(1, 1, "O")
a.update(1, 3, "X")
a.update(3, 3, "O")
a.update(3, 2, "X")
a.update(3, 1, "X")
a.update(3, 0, "X")
a.update(1, 0, "X")
a.update(1, 2, "X")
a.update(2, 0, " ")
a.update(2, 2, "X")
a.printOut()
c = b.detect(a.layoutArray)
print(c)


