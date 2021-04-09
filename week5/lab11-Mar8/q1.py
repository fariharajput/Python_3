# Question 1: Binary Search

# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
# Hint: You can use the .sort() function to sort this array

# Given a sorted array,

# Please implement the binary search algorithm that can search the number 43
#####################################


def binarySearch(num, list1, first, last):
    mid = (first + last)//2

    if list1[mid] == num:
        return mid
    elif list1[mid] > num:
        return binarySearch(num, list1, first, mid-1)
    else:
        return binarySearch(num, list1, mid+1, last)

    return -1


list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
num = 43
list1.sort()
print("Sorted list is ", list1)
print("list size is ", len(list1))
print("Number {0} found at index {1}".format(num, binarySearch(num, list1, 0, len(list1)-1)))
