import sys

n, l = map(int, sys.stdin.readline().split())
pipes = list(map(int, sys.stdin.readline().rstrip().split()))

pipes.sort()

tape = 1
dist = 0  
for i in range(1, n):
    dist += abs(pipes[i] - pipes[i - 1])
    if l > dist:
        continue
    else:
        tape += 1
        dist = 0
print(tape)