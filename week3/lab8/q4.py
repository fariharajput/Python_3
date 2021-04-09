# Question4: Let’s sort the array using Selection sort
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that
# takes list1 an input
# Sort all elements in the list in a descending order
# Returns the sorted list

# Hint: Check this video to learn more about selection sort: https://www.youtube.com/watch?v=xWBP4lzkoyM&ab_channel=GeeksforGeeks


# Note: You are not allowed to use the list build-in function .sort()

# function of selection sorting
def selectionSortFunc(list1):
    for i in range(len(list1)):
        posMax = i
        for j in range(i, len(list1)):
            if list1[j] > list1[posMax]:
                list1[j], list1[posMax] = list1[posMax], list1[j]
                posMax = i

    return list1


# main program
list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
print(selectionSortFunc(list1))
