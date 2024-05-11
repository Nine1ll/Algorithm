def solution(id_list, report, k):
    report_names = {}
    report_counts = {}
    for i_d in id_list:
        report_names[i_d] = []
        report_counts[i_d] = 0 
    
    for r in report:
        user_id, report_id = r.split(" ")
        if report_id not in report_names[user_id]:
            report_names[user_id].append(report_id)
            report_counts[report_id] += 1
    
    answer = [0] * len(id_list)

    for index, i in enumerate(id_list):
        for name in report_names[i]:
            if report_counts[name] >= k:
                answer[index] += 1
    return answer