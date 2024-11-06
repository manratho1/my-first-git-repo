#length of a string

def len_str(string1):
    length=0
    for _ in string1:
        length=length+1
    return length

string1="Hello"
print(len_str(string1))
