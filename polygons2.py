import turtle

x = input("How many sides?: ")
x = int(x)
a = (360 / x)

if x <= 0:
	print("Invalid input.")

else:
	s = input("Side length: ")
	s = int(s)
	
	for i in range(x):
		turtle.forward(s)
		turtle.left(a)

turtle.done()
