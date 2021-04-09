# Question3: Let’s sort the array using Bubble sort
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that
# takes list1 an input
# Sort all elements in the list in a descending order
# Returns the sorted list

# Hint: Check this video to learn more about bubble sort: https://www.youtube.com/watch?v=nmhjrI-aW5o&ab_channel=GeeksforGeeks


# Note: You are not allowed to use the list build-in function .sort()

def bubbleSortFunc(list1):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(list1)-1):
            if list1[i] < list1[i + 1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swap = True

    return list1


list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
print(bubbleSortFunc(list1))
