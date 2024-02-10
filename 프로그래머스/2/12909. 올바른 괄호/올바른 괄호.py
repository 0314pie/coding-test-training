def solution(s):
    a = []
    for i in s:
        if i == "(":
            a.append(i)
        elif i == ")":
            if '(' not in a:
                return False
            a.pop()
    
    return not a
            
                
                
    
    
   