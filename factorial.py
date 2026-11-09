


def factorial(n: int) -> int:
  """Calculates the factorial of a non-negative integer."""
  if not isinstance(n, int):
    raise TypeError("Input must be an integer.")
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  fact = 1
  for i in range(1, n + 1):
    fact *= i
  return fact


if __name__=="__main__":
     try:
            num=5
            print(factorial(num))


     except ValueError as e:
            print(e)
       
     except TypeError as e:
             print(e)
     
           

