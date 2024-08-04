import sys

n = int(sys.stdin.readline())
count=0
while count**2 < n:
    count+=1
    if n == 1:
        print(n)
        break
    elif count**2 > n:
        print(count -1)
    elif count**2 == n:
        print(count)
    else:
        continue