import math

def sqrt(x):
	if (x < 0):
		print("Positive inputs only")
	else:
		print(math.sqrt(x))

def asin(x):
	if (x > 1 or x < -1):
		print("Input must be between -1 and 1")
	else:
		print(math.asin(x))

def acos(x):
	if (x > 1 or x < -1):
		print("Input must be between -1 and 1")
	else:
		print(math.acos(x))

def atan(x):
	print(math.atan(x))
	
	
def main()
	func = input("Which function?\nsqrt = s\narcsin = a\narccos = c\narctan = t\n")

	inp = int(input("Enter number to calculate: "))
	
	if func == "s":
		sqrt(inp)

	elif func == "a":
		asin(inp)

	elif func == "c":
		acos(inp)

	elif func == "t":
		atan(inp)
		
		
if __name__ == "__main__":
	main()


