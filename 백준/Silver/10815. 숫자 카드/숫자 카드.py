import sys

n = int(sys.stdin.readline())
s_cards = list(map(int,sys.stdin.readline().split()))
dict_card = {}
for s_card in s_cards:
    dict_card[s_card] = 1

m = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))

answer = []
for card in cards:
    try:
        answer.append(dict_card[card])
    except KeyError:
        answer.append(0)

print(*answer)
