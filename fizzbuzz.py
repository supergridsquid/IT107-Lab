def div(abot):
	if (abot % 3 == 0) and (abot % 5 == 0):
		print (abot, " FizzBuzz")
	elif abot % 3 == 0:
		print (abot, " Fizz")
	elif abot % 5 == 0:
		print (abot, " Buzz")
	else:
		print (abot)



def main():
	top = int(input("Enter an number: "))
	bot = 1

	if top <=0:
		print("Not a positive number!")

	else:
		while bot <= top:		
			div(bot)
			bot += 1



if __name__ == "__main__":
	main()
