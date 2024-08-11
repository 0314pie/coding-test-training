def solution(arr, k):
    result = []
    for i in range(len(arr)):
        if len(result) == k:
            break;
        elif i == 0 :
            result.append(arr[0])
        elif arr[i] not in result:
            result.append(arr[i])
    
    if len(result) < k:
        result.extend([-1] * (k-len(result)))
            
    return result
        
        