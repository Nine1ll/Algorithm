import sys


def make_palindrom(alph):
    answer = ""
    sorted_key = sorted(alph.keys())
    for key in sorted_key:
        if alph[key] // 2 > 0:
            answer += key * (alph[key] // 2)
            alph[key] -= 2 * ( alph[key] // 2)

    mul_cnt = len(answer)
    for key in sorted_key:
        if alph[key] % 2 != 0:
            answer += key * alph[key]

    answer += answer[:mul_cnt][::-1]

    return answer


def is_it_palindrom(counts):
    odd = 0
    for cnt in counts:
        if cnt % 2 != 0:
            odd += 1

    if odd > 1:
        return False

    return True


alphabets = sys.stdin.readline().rstrip()
check_alphabets = {}

for alphabet in alphabets:
    try:
        check_alphabets[alphabet] += 1
    except KeyError:
        check_alphabets[alphabet] = 1

if is_it_palindrom(check_alphabets.values()):
    print(make_palindrom(check_alphabets))
else:
    print("I'm Sorry Hansoo")
