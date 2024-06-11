import sys

n = int(sys.stdin.readline())

div = 2
while True:
    if n == 1:
        break

    rest = n % div
    if rest != 0:
        div += 1
    else:
        n = n // div
        print(div)
