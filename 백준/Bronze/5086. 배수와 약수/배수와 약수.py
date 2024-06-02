import sys

options = ['factor', 'multiple', 'neither']


def check_faml(n1,n2):
    if n2 % n1 == 0:
        return options[0]
    elif n1 % n2 == 0:
        return options[1]
    else:
        return options[2]


answer = []
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        break
    answer.append(check_faml(a,b))
    
for ele in answer:
    print(ele)