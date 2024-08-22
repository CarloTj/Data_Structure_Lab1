num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
Num1 = int(num1)
Num2 = int(num2)
if num1 > num2:
    print(str(Num1) + " is less than " + str(num2))
elif num1 < num2:
    print(f"{Num1} is greater than {Num2}")
elif num1 == num2:
    print(str(Num1) + " is equal to " + str(Num2))
else:
    print("Error!")

# name1 = input("Enter Classmate name 1: ")
# name2 = input("Enter Classmate name 2: ")
# name3 = input("Enter Classmate name 3: ")
#
# print(f"Your Classmates are {name1} {name2} {name3}")
