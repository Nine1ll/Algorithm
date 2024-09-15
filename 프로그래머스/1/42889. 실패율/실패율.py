def solution(N, stages):
    '''
    실패율 : 클리어 못한 플레이어 수 / 스테이지 도달 플레이어 수
    실패율이 높은 스테이지부터 출력하는 함수
    '''
    failure = {key: 0 for key in range(1, N + 1)}
    player = [0 for _ in range(N + 2)]
    for stage in stages:
        player[stage] += 1

    for stage in range(1, N + 1):
        try:
            failure[stage] = player[stage] / sum(player[stage:])
        except ZeroDivisionError:
            failure[stage] = 0
    return sorted(failure, key=lambda x: failure[x], reverse=True)