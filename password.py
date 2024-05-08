password = False
addition = 1
lock = 3
numbers = 0
while not password:
    answer = input("Enter password")
    if answer == "school":
     password = True
     print("Correct password.")
    else:
     lock = lock - 1
     if lock != 0:
         print("Incorrect.",lock,"chances left")
     elif lock == 0:
         password = True
         print("Locked.")
         break
