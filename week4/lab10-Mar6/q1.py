# Question 1: Find factorial using recursion

# Example
# 5!= 5*4*3*2*1

# Write a program that
# takes an integer input from the user
# Finds factorial using recursive function
# prints the fictiorial value
##############################################################

# sudo code
# input from user
# repeate multiplication with all numbers uptil greater than 1
# print result

def extraLongFactorials(n):
    if n < 2:
        return 1

    return n * extraLongFactorials(n-1)
    


# main program
try:
    num = int(input("Enter a positive integer: "))
    print(extraLongFactorials(num))
except:
    print("You entered an invalid iteger")
