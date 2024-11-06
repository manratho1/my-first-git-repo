def find_dup(x):
    charseen=[]
    duplicates=[]
    for i in x:
        if i in charseen:
            if i not in duplicates:
                duplicates.append(i)    
        else:
            charseen.append(i)
    return duplicates

x=[4, 3, 2, 7, 8, 2, 3, 1]
print(find_dup(x))
