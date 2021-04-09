print('Question 1: Write a program that prints a square.')
# print("_________________________________")
# print("|\t\t\t\t|")
# print("|\t\t\t\t|")
# print("|\t\t\t\t|")
# print("|\t\t\t\t|")
# print("|\t\t\t\t|")
# print("|\t\t\t\t|")
# print("|_______________________________|")

length=15
for row in range(length):
    for col in range(length):
        if(row == 0 or row == length - 1 or col == 0 or col == length - 1):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()

# print('\nQuestion 2: A. Write a program that prints the following.')
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)
# print(11)
# print(12)
# print(13)
# print(14)
# print('\nQuestion 2: B. Write a program that prints the following.')
# for x in range(1, 15):
#   print(x)

# print('\nQuestion 3: 1. Take two Integer inputs from the user.')
# x = input("Enter first integer: ")
# y = input("Enter second integer: ")
# print("Fist integer is: ", x)
# print("Second integer is: ", y)

# print('\nQuestion 3: 2. Add two Integer inputs and prints the answer.')
# a = input("Enter first integer: ")
# b = input("Enter second integer: ")
# sum = int(a) + int(b)
# print("sum of integers is: ", sum)
