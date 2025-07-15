import output_handler as oh
import line_detecter as ld
a = oh.output_handler(4)
b = ld.line_detecter(4)
a.update(0, 2, "X")
a.update(1, 1, "O")
a.update(1, 3, "X")
a.update(3, 3, "O")
a.update(3, 2, "O")
a.update(3, 1, "O")
a.update(3, 0, "O")
a.printOut()
c = b.detect(a.layoutArray)
print(c)
