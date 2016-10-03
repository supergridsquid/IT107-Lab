import math

def circ(rad):
	diam = (2 * rad)
	circum = (diam * math.pi)
	print ("Circle circumference: ", circum)

	area = (math.pi * rad ** 2)
	print("Circle area: ", area)
		
def rect(h, w):
	perim = (2 * h + 2 * w)
	print("Rectangle perimeter: ", perim)
	
	area = (h * w)
	print("Rectangle area: ", area)

def squ(s):
	perim = (4 * s)
	print("Square perimeter: ", perim)

	area = (s ** 2)
	print("Square area: ", area)

def main():
	shape = int(input("For circle, enter 1\nFor rectangle, enter 2\nFor square, enter 3\n"))

	if shape == 1:
		rad = float(input("Input circle radius: "))
		circ(rad)

	elif shape == 2:
		h = float(input("Input rectangle height: "))
		w = float(input("Input rectangle width: "))
		rect(h, w)

	elif shape == 3:
		s = float(input("Input square side length: "))
		squ(s)

		
if __name__ == "__main__":
	main()
