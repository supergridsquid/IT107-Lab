def convert(measure):
    feet = measure * 3.281
    yards = measure * 1.094
    miles = measure * 0.0006214
    
    print ("The measurement in feet is:", feet)
    print ("In yards:", yards)
    print ("In miles:", miles)
    
    
def main():
    inp = float(input("Please type a measurement in meters: "))
    convert(inp)
    
if __name__ == "__main__":
    main()
