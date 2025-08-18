def solution(land):
    """
    열은 무조건 4개, 2차원 배열로 주어짐
    각 행의 한칸은 무조건 밟아야한다
    같은 열을 연속해서 밟을 수 없다. (4열 -> 4열 불가, 4열 -> 3열 -> 4열 가능 )
    밑으로 내려오면서 최대값을 얻을 수 있는 방법을 찾아라!
    """

    '''
    | 1 | 2 | 3 | 5 |

    | 10 | 11 | 12 | 11 |

    | 16 | 15 | 13 | 13 |
    
    '''
    # row_max = [0, 0, 0, 0]
    
    for row_num, row in enumerate(land):
        if row_num:
            # 이전 row에서 내 col을 제외한 다른 col의 max 값을 더함
            prev_row = land[row_num - 1]
            for i in range(4):
                row[i] += max(prev_row[:i] + prev_row[i+1:])

    return max(land[len(land)-1])