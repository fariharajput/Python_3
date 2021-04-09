def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                return False
            else:
                return True
    else:
        return False

def factors(num):
    fact = []
    for i in range(1, num + 1):
       if num % i == 0:
           fact.append(i)
    return fact

def prime_factors(num):
    prime_fact = []
    for i in num:
        if i == 2 or is_prime(i):
            prime_fact.append(i)

    return prime_fact[:-1]

num = int(input("Enter an integer: "))
# print(is_prime(num))
print(factors(num))
print(prime_factors(factors(num)))