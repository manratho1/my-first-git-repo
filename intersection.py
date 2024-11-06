arr1=[1,2,2,1]
arr2=[2,2]

result=[]
set1=set()

def intersection(arr1,arr2):
    for num in arr1:
        if num in arr2 and num not in set1:
            result.append(num)
            set1.add(num)
    return result

print(intersection(arr1,arr2))

