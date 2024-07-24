def solution(t, p):
    cnt =0
    a = len(p)
    
    for i in range(0, len(t)-a+1):
        b = t[i:i+a]
        if b <= p:
            cnt +=1
            
    return cnt