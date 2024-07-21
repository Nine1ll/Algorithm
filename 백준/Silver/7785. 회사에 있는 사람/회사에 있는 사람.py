import sys

n = int(sys.stdin.readline())
company = {}
for i in range(n):
    person, state = sys.stdin.readline().split()
    company[person] = 'in'
    if state == "leave":
        del company[person]

company = dict(sorted(company.items(), reverse=True))

for person in company.keys():
    print(person)
