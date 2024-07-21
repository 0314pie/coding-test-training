def solution(number):
    num = number.split()
    answer = 0 
    for i in num :
        answer += int(i)
    return answer % 9