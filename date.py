def monthCheck(mon):

	if mon == "January":
		return 0

	elif mon == "February":
		return 31

	elif mon == "March":
		return 59

	elif mon == "April":
		return 90

	elif mon == "May":
		return 120

	elif mon == "June":
		return 151

	elif mon == "July":
		return 181
	
	elif mon == "August":
		return 212

	elif mon == "September":
		return 243

	elif mon == "October":
		return 273

	elif mon == "November":
		return 304

	elif mon == "December":
		return 334

	else:
		return -1

def yearday(m, d):
	monthdays = monthCheck(m)
	if monthdays == -1:
		print ('error')

	else:
		
		if 0 < d <= 31:
			yearday = monthdays + d
			return yearday
		else:
			print ('error')

def main():
	month = input ("Enter month: ")
	day = int (input ("Enter day number: "))

	yd = yearday(month, day)
	print ('Day of the year: ', yd)
	

if __name__ == "__main__":
	main()
