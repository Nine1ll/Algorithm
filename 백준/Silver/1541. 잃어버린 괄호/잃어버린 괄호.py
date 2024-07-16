import sys

equation = sys.stdin.readline().rstrip().split("-")
for i in range(len(equation)):
    try:
        equation[i] = int(equation[i])
    except ValueError:
        equation[i] = list(map(int, equation[i].split("+")))

min_num = 0
try:
    min_num = sum(equation[0])
except TypeError:
    min_num = equation[0]

for i in range(1, len(equation)):
    try:
        min_num -= sum(equation[i])
    except TypeError:
        min_num -= equation[i]

print(min_num)