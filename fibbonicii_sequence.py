n=10
n = 10


def fibonacci_sequence(n: int) -> list[int]:
  a, b = 0, 1
  sequence = []
  for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence


fib_list = fibonacci_sequence(n)
print(fib_list)