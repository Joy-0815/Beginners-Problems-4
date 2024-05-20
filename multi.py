multi = int(input("Enter a positive number."))
numbs = False
times = 0

while not numbs:
    multi = int(input("Enter a positive number."))
    if multi <=0:
        print("Try again.")
    else:
        for num in range (0,999999999):
            times = times + 1
            print(multi*times)
