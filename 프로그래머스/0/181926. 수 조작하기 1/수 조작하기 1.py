def solution(n, control):
    con_list = list(control)
    
    for i in con_list:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == "d":
            n += 10
        elif i == 'a':
            n -= 10
    return n