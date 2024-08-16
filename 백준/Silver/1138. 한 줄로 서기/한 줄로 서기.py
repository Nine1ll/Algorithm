import sys

n = int(sys.stdin.readline())
seats = [0] * n
people = list(map(int, sys.stdin.readline().split()))
seats[people[0]] = 1

for i in range(1, n):
    front_higher = people[i]
    seat_count = 0
    for j, seat in enumerate(seats):
        if seat == 0:
            seat_count += 1

        if seat_count - 1 == front_higher and seat == 0:
            seats[j] = i + 1
print(*seats)