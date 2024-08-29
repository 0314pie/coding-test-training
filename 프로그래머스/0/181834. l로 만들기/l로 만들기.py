def solution(myString):
    answer = ""
    for a in myString:
        if ord(a) < ord("l"):
            answer += "l"
        else:
            answer += a
    return answer
            