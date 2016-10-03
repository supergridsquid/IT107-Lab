import turtle

def main():
	turtle.left(90)

	while 1 == 1:
		inp = input('Enter direction (up, down, left, right): ')

		if inp == 'up':
			turtle.forward(50)

		elif inp == 'down':
			turtle.backward(50)

		elif inp == 'left':
			degree = int(input('How many degrees: '))
			turtle.left(degree)

		elif inp == 'right':
			degree = int(input('How many degrees: '))
			turtle.right(degree)

		elif inp == 'stop':
			exit()



if __name__ == "__main__":
	main()




