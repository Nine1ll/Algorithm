import sys
from itertools import combinations, combinations_with_replacement

# 들어간 개수로만 숫자가 만들어짐.
# 그러면 개수를.. 흠.. 반복을 안해야하는데
n = int(sys.stdin.readline())
a = set([sum(ele) for ele in  list(combinations_with_replacement([1, 5, 10, 50], n))])
print(len(a))