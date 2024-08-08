def solution(myString):
    a = 0
    answer = []
    for i,v in enumerate(myString):
        if v == "x":
            answer.append(len(myString[a:i]))
            a = i+1
    answer.append(len(myString[a:]))
                          
    return answer
            