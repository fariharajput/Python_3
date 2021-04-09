# Question2: Let’s sort the array
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that
# takes list1 an input
# Sort all elements in the list in an ascending order
# Returns the sorted list

def list_func(list1):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(list1)-1):
            if list1[i] > list1[i + 1]:
                temp = list1[i]
                list1[i] = list1[i + 1]
                list1[i + 1] = temp
                swap = True

    # i = 0
    # while i < len(list1)-1:
    #     if list1[i] > list1[i+1]:
    #         temp = list1[i]
    #         list1[i] = list1[i + 1]
    #         list1[i + 1] = temp
    #         i = -1

    #     i += i

    return list1


list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
print(list_func(list1))
