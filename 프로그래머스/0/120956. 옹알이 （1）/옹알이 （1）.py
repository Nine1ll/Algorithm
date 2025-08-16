pronunciations = ["aya", "ye", "woo", "ma"]
    
def solution(babbling):
    
    # 1)모든 경우의 수 만들에서 그 안에 있는지 확인하면 되는거 아니야?
    # 순서 있음, 중복 불가 => 4 + 4*3 + 4*3*2 + 4*3*2*1 =>  64가지 경우의 수..?
    # 2)돌면서 나온거 표시하면서 삭제하면 될 것 같은데 ?
    answer = 0
    for word in babbling:
        for pronunce in pronunciations:
            word = word.replace(pronunce,"0")
        
        try:
            int(word)
            answer += 1
        except ValueError:
            continue

    return answer