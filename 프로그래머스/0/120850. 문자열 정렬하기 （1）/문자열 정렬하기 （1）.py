def solution(my_string):
    answer = []
    for char in my_string:
        try:
            answer.append(int(char))
        except ValueError:
            continue
    
    return sorted(answer)