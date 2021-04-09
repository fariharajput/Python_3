# Questions2: Let’s store data in dictionaries and arrays

# Write a program that asks a user to input the following details of ‘N’ number of students.
# Name
# Age
# Phone number
# Address
# Roll number
# nationality


# The program should save the data in the format that we discussed in the class

# final_list_students= [ dict, dict, dict, ….., dictN ]

# Where dict is {“name: “alan”, “age”: 12, … }

# Hint: write a program that converts all information of one student in a dictionary.
# Repeat that program for the ‘N’ number of students.
######################################################

# function to add record
def addRecord(Name, Age, Phone_number, Address, Roll_number, nationality):
    record = {
        'Name': Name,
        'Age': Age,
        'Phone_number': Phone_number,
        'Address': Address,
        'Roll_number': Roll_number,
        'Nationality': nationality
    }

    return record


######################################
# main program
num = int(input("How much data you have: "))
final_list_students = []

try:
    for record in range(num):
        print("Enter Record {0}:".format(record+1))
        print('-----------------------')
        Name            = input("Enter Name {0}: ".format(record+1))
        Age             = input("Enter Age{0}: ".format(record+1))
        Phone_number    = input("Enter Phone Number{0}: ".format(record+1))
        Address         = input("Enter Address{0}: ".format(record+1))
        Roll_number     = input("Enter Roll_number{0}: ".format(record+1))
        nationality     = input("Enter Nationality{0}: ".format(record+1))
        print('-----------------------')
        final_list_students.append(
            addRecord(Name, Age, Phone_number, Address,
                      Roll_number, nationality)
        )
except:
    print("Invalid input, Enter intigers only")

print(final_list_students)
