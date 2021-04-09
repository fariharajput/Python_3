# Question 1: Let’s sort the array using Insertion Sort
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that
# takes list1 an input
# Sort all elements in the list in an ascending order
# Returns the sorted list


# Hint: Check this video to learn more about insertion sort:
# https://www.youtube.com/watch?v=OGzPmgsI-pQ&ab_channel=GeeksforGeeks

# Note: You are not allowed to use the list build-in function .sort()

# Deliverables:
# Pseudo-code
# code
###############################################################################################

# Pseudo-code
# mark list in two categories left side sorted and right side unsorted

# firstly choose index[0] element as sorted

# move cursor to index[1]
# compare index[1] with inde[0] (all sorted items) and place it on correct index and mark as sorted

# move cursor to index[2]
# compare index[2] with inde[0], index[1] (all sorted items) and place it on correct index and mark as sorted

# move cursor to index[3]
# compare index[3] with inde[0], index[1], ... (all sorted items) and place it on correct index and mark as sorted

# and so on....

def insertionSort(list1):
    for i in range(1, len(list1)):
        val = list1[i]
        pos = i - 1

        while pos >= 0 and val < list1[pos]:
            list1[pos + 1] = list1[pos]
            pos -= 1

        list1[pos + 1] = val

    return list1


# main program
list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
print('unsorted list is {0}'.format(list1))
print('  sorted list is {0}'.format(insertionSort(list1)))
