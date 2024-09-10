import sys
from collections import deque

s = sys.stdin.readline().strip() + ' '
words = deque([])
answer = ""
in_bracket = False

for char in s:
    if char == "<":
        in_bracket = True
        for _ in range(len(words)):
            answer += words.pop()

    words.append(char)

    if char == ">":
        in_bracket = False
        for _ in range(len(words)):
            answer += words.popleft()

    if char == " " and not in_bracket:
        words.pop()
        for _ in range(len(words)):
            answer += words.pop()
        answer += " "
print(answer)