import sys


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    else:
        return n


answer = 0
for i in range(3, 0, -1):
    s = sys.stdin.readline().rstrip()
    try:
        s = int(s)
        answer = s + i
    except ValueError:
        continue
print(fizzbuzz(answer))
