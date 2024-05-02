def solution(genres, plays):
    count = {}
    for i, g in enumerate(genres):
        if g in count:
            count[g][1] += plays[i]
            count[g][0].append(i)
        else:
            count[g] = [[i], plays[i]]

    music = sorted(count.items(), key=lambda x: x[1][1], reverse=True)
    
    answer = []
    for item in music:
        item[1][0] = sorted(item[1][0], key = lambda x: plays[x], reverse=True)
        answer += item[1][0][:2]
    
    return answer