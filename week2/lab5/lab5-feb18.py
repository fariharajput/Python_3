# Question 1: The Collatz Conjecture

import random
n = int(input("Please enter a positive number: "))
chain = []

if n > 0:
    chain.append(n)
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
            chain.append(n)
        else:
            n = int(n * 3 + 1)
            chain.append(n)
else:
    print("Please enter positive integer")

print("The collatz chain is:", end=' ')
for i in chain:
    print(i, end=' - ')

print("\nCollatz chain Length is:", len(chain))

# Question 2: Nested loops

long_flag = int(input("How long is your flag? - "))
wide_flag = int(input("How wide is your flag? - "))
long_flagpole = int(input("How long is your flagpole? - "))
wide_flagpole = int(input("How wide is your flagpole? - "))

for i in range(long_flag):
    print("*" * wide_flag)

for j in range(long_flagpole):
    print("*" * wide_flagpole)

# Question 3: Lucky 7 in LUDO
import random

roll = int(input("How many times would you like to roll the dice? - "))
sums = []

print()

for i in range(roll):
    dice = (random.randint(1, 6), random.randint(1, 6))
    print(dice)
    sums.append(sum(dice))
    print("Dice roll {0} sum: {1}".format(i+1, sum(dice)))

print("\nYou rolled lucky seven {0} time(s)!".format(sums.count(7)))
