# Question 1: At what index is the

# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that takes in two inputs
# A “number”
# “list1”

# The function finds the index of the “number” in “list1”.
# The function should return the index number.

def find_func(num, list1):
    for i in range(len(list1)):
        if list1[i] == num:
            return i

list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
num = 68

print("Number {0} is at {1} index in list".format(num, find_func(num, list1)))