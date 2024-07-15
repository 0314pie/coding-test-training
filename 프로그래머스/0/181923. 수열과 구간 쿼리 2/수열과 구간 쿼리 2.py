def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        min_val = None 
        found = False
        
        for i in range(s, e + 1):
            if arr[i] > k:
                if min_val is None or arr[i] < min_val:
                    min_val = arr[i]
                    found = True
                
        if found:
            answer.append(min_val)
        else:
            answer.append(-1)
    
    return answer