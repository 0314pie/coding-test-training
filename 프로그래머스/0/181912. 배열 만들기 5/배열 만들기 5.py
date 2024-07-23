def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        a = int(str[s:s+l])
        if a > k:
            answer.append(a)
    return answer