import date

def horoCalc(d):
	AriesS = date.yearday("March", 21)
	AriesE = date.yearday("April", 19)

	TaurusS = date.yearday("April", 20)
	TaurusE = date.yearday("May", 20)

	GeminiS = date.yearday("May", 21)
	GeminiE = date.yearday("June", 20)

	CancerS = date.yearday("June", 21)
	CancerE = date.yearday("July", 22)

	LeoS = date.yearday("July", 23)
	LeoE = date.yearday("August", 22)

	VirgoS = date.yearday("August", 23)
	VirgoE = date.yearday("September", 22)

	LibraS = date.yearday("September", 23)
	LibraE = date.yearday("October", 22)

	ScorpioS = date.yearday("October", 23)
	ScorpioE = date.yearday("November", 21)

	SagittariusS = date.yearday("November", 22)
	SagittariusE = date.yearday("December", 21)
	
	AquariusS = date.yearday("January", 20)
	AquariusE = date.yearday("February", 18)

	PiscesS = date.yearday("February", 19)
	PiscesE = date.yearday("March", 20)

	CapricornS1 = date.yearday("December", 22)
	CapricornE1 = date.yearday("December", 31)
	CapricornS2 = date.yearday("January", 1)
	CapricornE2 = date.yearday("January", 19)


	if AriesS <= d <= AriesE:
		print("You are an Aries")

	elif TaurusS <= d <= TaurusE:
		print("You are a Taurus")

	elif GeminiS <= d <= GeminiE:
		print("You are a Gemini")

	elif CancerS <= d <= CancerE:
		print("You are a Cancer")

	elif LeoS <= d <= LeoE:
		print("You are a Leo")

	elif VirgoS <= d <= VirgoE:
		print("You are a Virgo")

	elif LibraS <= d <= LibraE:
		print("You are a Libra")

	elif ScorpioS <= d <= ScorpioE:
		print("You are a Scorpio")

	elif SagittariusS <= d <= SagittariusE:
		print("You are a Sagittarius")

	elif AquariusS <= d <= AquariusE:
		print("You are an Aquarius")

	elif PiscesS <= d <= PiscesE:
		print("You are a Pisces")

	elif CapricornS1 <= d <= CapricornE1 or CapricornS2 <= d <=CapricornE2:
		print("You are a Capricorn")



def main():
	day = int(input("Enter the day of the year: "))
	horoCalc(day)


if __name__ == '__main__':
	main()
