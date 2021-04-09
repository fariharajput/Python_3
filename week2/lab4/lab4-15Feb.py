# # Question 1: Calculate Factorial

# num = int(input("Enter a positive integer: "))
# factorial = 1

# if num < 0:
#     print("Invalid number")
# elif num == 0 or num == 1:
#     print("Factorial is ", factorial)
# else:
#     while num > 0:
#         factorial = factorial * num
#         num = num - 1
#     print("Factorial is ", factorial)

# Question 2: Print the following patterns using loop :

# a.
# for row in range(1, 5):
#     for col in range(row):
#         print("*", end="")
#     print()
# count = 1
# while count <= 4:
#     print("*" * count)
#     count = count + 1

# count = 1
# space = 2
# while count <= 5:
#     if count < 5:
#         print(" " * space + "*" * count)
#         count = count + 2
#         space = space - 1
#     if count >= 5:
#         print(" " * space + "*" * count)
#         count = count - 2
#         space = space + 1

# # b.
# for row in range(-2, 3):
#     for col in range(-2, 3):
#         if abs(row) == 0 or abs(col) == 0 or abs(row) == abs(col) and abs(row) < 2:
#             print('*', end='')
#         else:
#             print(' ',  end='')
#     print()

# c.


# # Question 3: Calculate the average

# userInput = ''
# numList = []

# while userInput != 'q':
#     userInput = input("Enter an integer or q to quit: ")
#     if userInput.isdigit():
#         numList.append(int(userInput))
#     else:
#         print("Please enter a valid number")

# averageNum = sum(numList)/len(numList)
# print("Your numbers are: ", numList)
# print("List average is: ", averageNum)

# i = 0
# productNum = 1
# while i < len(numList):
#     productNum = productNum * numList[i]
#     i = i + 1
# print("Product is ", productNum)

# # Question 4: Calculate the average

# my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
# averageNum = sum(my_list)/len(my_list)
# print("Average of list is: ", averageNum)

