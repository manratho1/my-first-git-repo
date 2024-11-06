def max_min(numbers):
    min_val=numbers[0]
    max_val=numbers[0]

    for num in numbers[1:]:
        if num<min_val:
           min_val=num
        if num>max_val:
           max_val=num
    
    return min_val, max_val

numbers=[7,2,3,4,5,0]
min_val,max_val=max_min(numbers)
print("Min_val:",min_val)
print("Max_val:",max_val)
