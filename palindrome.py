x=121
def palindrome(x):
    if x<0:
     return False
    else:
       return str(x)==str(x)[::-1]

print(palindrome(x))     