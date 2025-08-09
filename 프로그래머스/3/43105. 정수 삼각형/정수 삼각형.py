def solution(triangle):
    for i in range(len(triangle)-1):
        prev_line = triangle[i] 
        present_line = triangle[i+1]

        for j in range(len(present_line)):

            if j == 0:
                present_line[j] = prev_line[j] + present_line[j]
            elif j == len(present_line)-1:
                present_line[j] = prev_line[j-1] + present_line[j]
            else:
                present_line[j] = max( prev_line[j-1] + present_line[j], prev_line[j] + present_line[j])
    
    return max(triangle[-1])