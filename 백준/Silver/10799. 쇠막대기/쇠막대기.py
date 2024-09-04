import sys

stack = []
sticks = sys.stdin.readline().rstrip()
# stack에 (를 넣고 )가 입력되면 빼면서 (남은 개수를 추가하면 될 것 같은데
answer = 0
for index, stick in enumerate(sticks):
    if stick == "(":
        stack.append(stick)
    else: # stick = ")"
        if sticks[index - 1] == "(":
            stack.pop()
            answer += len(stack)
        else: # stick == ")"
            stack.pop()
            answer += 1

print(answer)