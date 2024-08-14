import sys

t = int(sys.stdin.readline())
fibonacci = [[0,0]]*2
fibonacci[0] = [1, 0]
fibonacci[1] = [0, 1]
n_list = []
for _ in range(t):
    n_list.append(int(sys.stdin.readline()))
for i in range(2, 41):
    fibonacci.append([fibonacci[i-1][0] + fibonacci[i-2][0], fibonacci[i-1][1] + fibonacci[i-2][1]])

for n in n_list:
    print(*fibonacci[n])