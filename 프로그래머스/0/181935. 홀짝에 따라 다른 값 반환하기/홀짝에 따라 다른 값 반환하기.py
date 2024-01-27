def solution(n):
    num = 0
    if n % 2 ==1:
        for a in range(1,n+1):
            if a %2 ==1:
                num = num + a
    elif n % 2 ==0:
        for a in range(1,n+1):
            if a % 2 ==0:
                num = num + (a **2)
    return num
                
