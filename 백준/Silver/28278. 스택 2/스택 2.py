import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if order[0] == "1":
        _, x = order.split()
        stack.append(int(x))
    elif order[0] == "2":
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    elif order[0] == "3":
        print(len(stack))
    elif order[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        try:
            print(stack[-1])
        except IndexError:
            print(-1)
