def sum_of_digits(number):
    total=0
    for digit in str(number):
        total=total+int(digit)
    return total

number=1234
print(sum_of_digits(number))
    

