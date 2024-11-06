def prime_or_not(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if (num % i) == 0:
           return "not a Prime"
    return "prime"
            
print(prime_or_not(43))

