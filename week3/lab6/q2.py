def checkXOR(A, B):
    if A.title() == 'False' and B.title() == 'False':
        return False
    elif A.title() == 'False' and B.title() == 'True':
        return True
    elif A.title() == 'True' and B.title() == 'False':
        return True
    elif A.title() == 'True' and B.title() == 'True':
        return False
    else:
        return "Wrong entery"

    # if A == B:
    #     return "False"
    # else:
    #     return "True"


inputA = input("Enter 'True' or 'False': ")
inputB = input("Enter 'True' or 'False': ")

print("XOR result: ", checkXOR(inputA, inputB))