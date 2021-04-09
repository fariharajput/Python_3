# Question1: Change data structures

# names= ['alan', 'john', 'tania', 'ahmad', 'ali', 'muddassar', 'raheel', 'hamza']
# age= [12,13,14,15,17,16,13,13]

# Write a function that converts the above data in the following format.

# people = [ {'name': 'alan', 'age': 12}, {'name': 'john', 'age': 13}, ……]

def converData(names, ages):
    people_list = []

    # for name, age in zip(names, ages):
    #     people = {'name': name, 'age': age}
    for i in range(len(names)):
        people = {}
        people['name'] = names[i]
        people['age'] = ages[i]
        people_list.append(people)

    return people_list


names = ['alan', 'john', 'tania', 'ahmad',
         'ali', 'muddassar', 'raheel', 'hamza']
ages = [12, 13, 14, 15, 17, 16, 13, 13]

print(converData(names, ages))
