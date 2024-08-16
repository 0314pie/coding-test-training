def solution(picture, k):
    a = []
    answer = []
    for pic in picture:
        for i in pic:
            a.append(i * k)
        answer.extend(["".join(a)] * k)
        a = []
            
    return answer