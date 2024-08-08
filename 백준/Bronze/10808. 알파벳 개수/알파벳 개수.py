import sys

s = sys.stdin.readline()

alph = []
for i in range(97, 122 + 1):
    alph.append(s.count(chr(i)))

print(*alph)