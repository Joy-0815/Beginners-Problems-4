password = False
number = False
addition = 1
lock = 3
numbers = 0
while not password:
    answer = input("Enter password")
    if answer == "school":
     password = True
     print("Correct password.")

    else:
         while not number:
             numbers = numbers + addition 
             print("Incorrect.",lock-numbers,"chances left.")
             if numbers == 0:
                 number = True
                 print("Locked.")
                 break