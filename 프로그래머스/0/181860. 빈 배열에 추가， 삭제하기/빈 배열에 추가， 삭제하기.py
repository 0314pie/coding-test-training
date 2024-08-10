def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i]:  
            X.extend([arr[i]] * (2 * arr[i]))  
        else:  
            X = X[:-arr[i]] 
            
    return X
