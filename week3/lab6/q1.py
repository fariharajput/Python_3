def ascii_sum(txt):
    sum = 0
    for x in txt:
        sum = sum + ord(x)

    return sum

def ascii_sum_odd(txt):
    sum = 0
    for x in txt:
        x = ord(x)
        if  x % 2 != 0:
            sum = sum + x

    return sum

def ascii_sum_even(txt):
    sum = 0
    for x in txt:
        x = ord(x)
        if  x % 2 == 0:
            sum = sum + x

    return sum

txt = input("Enter a String: ")
print("Total ASCII Sum: ", ascii_sum(txt))
print("ASCII Sum of Odd Numbered Characters: ", ascii_sum_odd(txt))
print("ASCII Sum of Even Numbered Characters: ", ascii_sum_even(txt))