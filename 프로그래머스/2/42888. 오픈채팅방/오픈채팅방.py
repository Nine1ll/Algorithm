def solution(record):
    usr = {}
    for line in record:
        cmd = line.split(" ")
        if cmd[0] != "Leave":
            usr[cmd[1]] = cmd[2]
    
    answer = []            
    for line in record:
        cmd = line.split(" ")
        user_name = usr[cmd[1]]
        if cmd[0] == "Enter":
            answer.append(f"{user_name}님이 들어왔습니다.")
        elif cmd[0] == "Leave":
            answer.append(f"{user_name}님이 나갔습니다.")

    return answer