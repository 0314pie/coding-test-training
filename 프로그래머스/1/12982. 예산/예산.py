def solution(d, budget):
    d = sorted(d)
    cnt = 0
    for i in d:
        if budget >= i:
            budget -= i
            cnt += 1
    return cnt