# Question2: Reading and Writing from a    file.

# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
# Hint: You can use the .sort() function to sort this array

# Write a program that can
# Write the sorted array in an “array. txt” file.


# Then write a program that can
# Read the data from “array.txt” file
# Increase every number by 5
# Save all new numbers back in “array.txt” file.
###########################################################

list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
list1.sort()

array_file = open('array.txt', 'w')
for i in range(len(list1)):
    array_file.write(str(list1[i]) + '\n')

print("array file ")
array_file = open('array.txt', 'r')
array_data = array_file.read()
print(array_data)

print("\narray file after increase of 5")
array_file = open('array.txt', 'a')
for i in range(len(list1)):
    appended_num = list1[i] + 5
    array_file.write(str(appended_num) + '\n')

print("\nappended file ")
array_file = open('array.txt', 'r')
array_data = array_file.read()
print(array_data)

array_file.close
