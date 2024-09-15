import sys

n = int(sys.stdin.readline())
house_coordinate = list(map(int, sys.stdin.readline().split()))
house_coordinate.sort()
print(house_coordinate[(n-1)//2])