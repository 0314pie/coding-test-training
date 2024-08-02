def solution(arr):
    if 2 not in arr:
        return [-1]
    
    a = []
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
    
    if len(a) < 2:
        return [2]
    
    return arr[a[0]:a[-1] + 1]

    
            
        