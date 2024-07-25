import sys

n = int(sys.stdin.readline())  # n <= 10
words = []
alph = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)

# 각 알파벳의 가중치 계산
for word in words:
    length = len(word)
    for i in range(length):
        if word[i] in alph:
            alph[word[i]] += 10 ** (length - i - 1)
        else:
            alph[word[i]] = 10 ** (length - i - 1)

# 가중치가 큰 순서대로 알파벳 정렬
sorted_alph = sorted(alph.items(), key=lambda x: x[1], reverse=True)

# 숫자 할당
number = 9
alph_to_number = {}
for item in sorted_alph:
    alph_to_number[item[0]] = number
    number -= 1

# 단어를 숫자로 변환하고 합 계산
total_sum = 0
for word in words:
    number_string = ""
    for c in word:
        number_string += str(alph_to_number[c])
    total_sum += int(number_string)

print(total_sum)
