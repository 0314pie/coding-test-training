def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        num_str = str(i)
        valid = True
        for j in num_str:
            if j != "0" and j != "5":
                valid = False
                break
        if valid:
            answer.append(i)
    
    if not answer:
        return [-1]
    
    return answer