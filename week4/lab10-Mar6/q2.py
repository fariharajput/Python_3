# Question 2: Let’s sort the array using Merge Sort
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that
# takes list1 an input
# Sort all elements in the list in an ascending order
# Returns the sorted list


# Hint: Check this video to learn more about merge sort: https://www.youtube.com/watch?v=JSceec-wEyw&ab_channel=GeeksforGeeks

# Note: You are not allowed to use the list build-in function .sort()

# Deliverables:
# Pseudo-code
# Code

# Hint:  Use recursion

##############################################################################################


# Pseudo-code
# divide the list into two parts
# divide each part of the list into two parts
# divide every child part until > 1
# sort last two elements
# then join two parts and sort
# and so on

# Code

def merge(left, right):
    leftSide, rightSide = 0, 0
    list1 = []
    while leftSide < len(left) and rightSide < len(right):
        if left[leftSide] < right[rightSide]:
            list1.append(left[leftSide])
            leftSide = leftSide + 1
        else:
            list1.append(right[rightSide])
            rightSide = rightSide + 1

    list1 = list1 + left[leftSide:]
    list1 = list1 + right[rightSide:]

    return list1


def mergeSort(list1):
    if len(list1) <= 1:
        return list1

    # divide array in half and merge sort recursively
    mid = len(list1) // 2
    left = mergeSort(list1[:mid])
    right = mergeSort(list1[mid:])

    return merge(left, right)


# main program
list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
print('unsorted list is {0}'.format(list1))
print('  sorted list is {0}'.format(mergeSort(list1)))
