import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
times = []
for _ in range(n):
    start_time, end_time = map(int, sys.stdin.readline().split())
    times.append([start_time, end_time])

times.sort()
classroom = []
first_end_time = times[0][1]
heappush(classroom, first_end_time)

for i in range(1, n):
    next_start_time = times[i][0]
    if next_start_time < classroom[0]: # 처음 수업이 끝나는 시간과 다음 수업이 시작하는 시간을 확인해
        # 만약에 다음 수업 시작이 더 빠르면, 교실을 하나 더 잡아야헤 == classroom에 끝 시간 넣는다.
        heappush(classroom, times[i][1])
    else: # 만약에 다음 수업 시작이 더 느리면, 교실은 그냥 써도 되 == classroom에 있는 전 끝 시간을 다음 끝 시간으로 교체한다.
        heappop(classroom)
        heappush(classroom, times[i][1])

print(len(classroom))