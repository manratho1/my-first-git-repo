def uniquechar(input):
    charseen=""
    count=0
    for char in input:
        if char not in charseen:
            charseen=charseen+char
            count=count+1
    return charseen,count
    
Input= "abcabcbb"
output=uniquechar(Input)
print(output)
