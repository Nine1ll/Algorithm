def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {id : [[],0] for id in id_list}
    report = set(report)

    for r in report:
        user_id, report_id = r.split(" ")
        reports[user_id][0].append(report_id)
        reports[report_id][1] += 1

    for index, i in enumerate(id_list):
        for name in reports[i][0]:
            if reports[name][1] >= k:
                answer[index] += 1 
                
    return answer