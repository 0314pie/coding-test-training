def solution(arr, intervals):
    answer = []
    for start, end in intervals:
        for i in range(start, end + 1):
            answer.append(arr[i])
    return answer