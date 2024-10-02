import sys
from collections import Counter

n = int(sys.stdin.readline())
books = []
for _ in range(n):
    books.append(sys.stdin.readline().strip())
books = Counter(books)
max_sell = max(books.values())
answer = []
for book, sell_cnt in books.items():
    if sell_cnt == max_sell:
        answer.append(book)

answer.sort()
print(answer[0])