x=[2,7,11,15]
l=len(x)

def numinlist(x):
    for i in range(l):
        if (i+1==l):
            y=x[i]+x[0]
            if y==9:
                return i,0
        else:
            z=x[i]+x[i+1]
            if z==9:
                return i,i+1
                

f=numinlist(x)
print(f)
