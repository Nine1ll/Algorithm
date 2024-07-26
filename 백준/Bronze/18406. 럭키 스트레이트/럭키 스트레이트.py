import sys

n = sys.stdin.readline().rstrip()
front = n[:len(n)//2]
back = n[len(n)//2:]

result = 0
for c in front:
    result += int(c)

for d in back:
    result -= int(d)

if result == 0:
    print("LUCKY")
else:
    print("READY")
