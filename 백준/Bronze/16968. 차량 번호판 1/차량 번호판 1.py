import sys

number_format = sys.stdin.readline().rstrip()
num_count = {'c': 26, 'd': 10}

front_format = number_format[0]
answer = num_count[front_format]

for i in range(1, len(number_format)):
    rear_format = number_format[i]
    if rear_format != front_format:
        answer *= num_count[rear_format]
    else:
        answer *= (num_count[rear_format] - 1)
    front_format = number_format[i]
print(answer)