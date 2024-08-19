def solution(arr):
    a = min(arr)
    arr.remove(a)
    if len(arr) <= 1:
        return [-1]
    return arr