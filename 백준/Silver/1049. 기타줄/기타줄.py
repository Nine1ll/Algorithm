import sys
from math import ceil

n, brand = map(int, sys.stdin.readline().split())  # buy or replace
min_package, min_one = 1000, 1000
for _ in range(brand):
    package, one = map(int, sys.stdin.readline().split())
    if package < min_package:
        min_package = package

    if one < min_one:
        min_one = one

package_num = ceil(n / 6)
print(min(min_one * n, package_num * min_package, min_package * (n // 6) + min_one * (n % 6)))