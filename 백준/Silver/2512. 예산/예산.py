import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum_budget = 0
        for budget in array:
            if budget <= mid:
                sum_budget += budget
            else:
                sum_budget += mid
        if sum_budget <= target:
            start = mid + 1
        elif sum_budget > target:
            end = mid - 1

    return end


n = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
budgets.sort()
m = int(sys.stdin.readline())

if sum(budgets) <= m:
    print(budgets[-1])
else:
    print(binary_search(budgets, m, 1, budgets[-1]))