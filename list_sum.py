list_nums=[1,2,3,4,5]
def count_list(list1):
    count=0
    for num in list_nums:
        count=count+num
    return(count)

x=count_list(list_nums)
print(x)
