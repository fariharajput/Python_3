# Question 1: Let’s build a calculator.

# Write a program that takes the following inputs
# Two numbers
# One operator ( +, -, *, /, or %)

# The program then should perform the operation on two numbers and should print an answer.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
choice = input("What do you want  ( +, -, *, /, or %): ")

num1 = float(num1)
num2 = float(num2)

if choice == '+':
    result = num1 + num2
elif choice == '-':
    result = num1 - num2
elif choice == '*':
    result = num1 * num2
elif choice == '/':
    result = num1 / num2
elif choice == '%':
    result = int(num1) % int(num2)
else:
    print("Wrong choice")

print(result)


# Question 2: Attendance checker

# A student will not be allowed to sit in an exam if his/her attendance is less than 75%.

# Write a program that takes the following input from a user
# Number of classes held
# Number of classes attended.

# And prints
# percentage of class attended
# If a student is allowed to sit in the exam or not.

classes = input("Enter Number of classes held: ")
attended = input("Enter Number of classes attended: ")

classes = int(classes)
attended = int(attended)

print("Enter Number of classes held: ", classes)
print("Enter Number of classes attended: ", attended)

perAttnd = attended / classes * 100

if perAttnd < 75:
    print("Your attendance percentage is {0}%, which is below, sorry! you are not allowed to sit in exam.".format(attended))
else:
    print("Your attendance percentage is {0}%, perfect, welcome! you are allowed to sit in exam.".format(attended))
