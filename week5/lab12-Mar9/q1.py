# Question 1: Jump Search

# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
# Hint: You can use the .sort() function to sort this array

# Given a sorted array,

# Please implement the Jump search algorithm that can search the number 43

# Hint: Please check out this video:
# https://www.youtube.com/watch?v=63kS6ZkMpkA&ab_channel=GeeksforGeeks

########################################################################

#main program
list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
list1.sort()

import math
num = 43  # number to be found

jump = int(math.sqrt(len(list1)))

min_index = 0
max_index = min_index + jump-1

flag = True

while flag:
    if num <= list1[max_index]:
        flag = False
    else:
        min_index = max_index
        max_index = max_index + jump-1
        if max_index > (len(list1)-1):
            max_index = len(list1)-1
            flag = False

print("Sorted list is \t",list1)
print("jump is \t",jump)
print("min index is \t",min_index)
print("max index is \t",max_index)

index = min_index

for i in list1[min_index:max_index+1]:
    if i == num:
        print("{0} is found at index {1}".format(num, index))
    index += 1