# Question2: Inserting in an array

# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
# Hint: You can use the .sort() function to sort this array

# Write a program that can insert an element the number 10
# in the right position in the sorted array.
############################################################

#main program

list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
num = 10
list1.sort()

print("Sorted list \t{0}".format(list1))

list1.append(num)

print("Updated list \t{0}".format(list1))
