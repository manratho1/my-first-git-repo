#print a palindrome string

text="radar"

def palindrome(string):
    string1=string[::-1]
    if string==string1:
        return("True")
    else:
        return("false")

check_pal=palindrome(text)
print(check_pal)

