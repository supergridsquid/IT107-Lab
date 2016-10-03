import math

shape = input("For circle, enter 1\nFor rectangle, enter 2\nFor square, enter 3\n")
shape = int(shape)

if shape == 1:
	rad = input("Input circle radius: ")
	rad = float(rad)

	diam = (2 * rad)
	circ = (diam * math.pi)
	circ = str(circ)
	print ("Circle circumference: " + circ)
	
	area = (math.pi * rad ** 2)
	area = str(area)
	print("Circle area: " + area)

elif shape == 2:
	h = input("Input rectangle height: ")
	h = float(h)
	w = input("Input rectangle width: ")
	w = float(w)

	perm = (2 * h + 2 * w)
	perm = str(perm)
	print("Rectangle perimeter: " + perm)

	area = (h * w)
	area = str(area)
	print("Rectangle area: " + area)

elif shape == 3:
	s = input("Input square side length: ")
	s = float(s)
	
	perm = (4 * s)
	perm = str(perm)
	print("Square perimeter: " + perm)

	area = (s ** 2)
	area = str(area)
	print("Square area: " + area)

