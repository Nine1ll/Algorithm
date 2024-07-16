import sys
n = int(sys.stdin.readline())
cords = list(map(int, sys.stdin.readline().split()))
cords2 = []
for i in range(n):
    cords2.append([cords[i], i])

cords2.sort()
index = 0
for i in range(0, len(cords2)-1):
    cords2[i].append(index)
    if cords2[i][0] == cords2[i+1][0]:
        continue
    else:
        index += 1

cords2[-1].append(index)

for i in cords2:
    i[0], i[1] = i[1], i[0]

cords2.sort()
for i in cords2:
    print(i[2])