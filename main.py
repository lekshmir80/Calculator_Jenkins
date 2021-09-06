from calc import Calculator
import add
import sub
import mul
import div
import sys

print(sys.argv)
if sys.argv[1] == "1":
	add.add(1,2)
elif sys.argv[1] == "2":
	sub.sub(4,2)
elif sys.argv[1] == "3":
	mul.mul(4,2)
elif sys.argv[1] == "4":
	div.div(4,2)

