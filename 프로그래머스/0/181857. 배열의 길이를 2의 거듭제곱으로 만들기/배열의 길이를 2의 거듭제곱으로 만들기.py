def solution(arr):
    n = len(arr)
    
    two = 1
    while two < n:
        two *= 2

    while len(arr) < two:
        arr.append(0)
    
    return arr