n=6
def Factorial_Recursion(n:int)->int:
     if n==0 or n==1:  

      return 1
     return  n * Factorial_Recursion(n-1)
print(Factorial_Recursion(n))

