# 닉네임은 마지막만 기억하면 되는거고, userid의 행동들은 순서대로 기억해야함.
# userid : 행동은 순서대로 기억하되, userid : 닉네임은 마지막만 기억해서 출력.
def solution(record):
    uid_nick = {}
    answer = []
    for log in record:
        command = log.split(" ")
        if command[0] != "Leave":
            uid_nick[command[1]] = command[2]
        
    for log in record:
        command = log.split(" ")
        if command[0] == "Enter":
            answer.append(f"{uid_nick[command[1]]}님이 들어왔습니다.")
        elif command[0] == "Leave":
            answer.append(f"{uid_nick[command[1]]}님이 나갔습니다.")
            
    return answer