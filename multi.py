multi = int(input("Enter a positive number."))
numbs = False
times = 0

while not numbs:
    multi = int(input("Enter a positive number."))
    if multi <=0:
        print("Please enter a positive number, not a negative number.")
    else:
        numbs = True
        for num in range (0,inf):
            times = times + 1
            print(multi*times)
