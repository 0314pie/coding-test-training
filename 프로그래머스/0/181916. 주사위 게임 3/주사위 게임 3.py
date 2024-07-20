def solution(a, b, c, d):
    dice = [a,b,c,d]
    
    unique = list(set(dice))
    
    if len(unique) == 1:
        return 1111 * unique[0]
    elif len(unique) == 2:
        one = dice.count(unique[0])
        two = dice.count(unique[1])
        
        if one == 3:
            return  (10 * unique[0] + unique[1])**2
        elif two == 3:
            return  (10 * unique[1] + unique[0])**2
        elif one ==2 and two ==2:
            return  (unique[1] + unique[0]) * abs(unique[1] - unique[0])
        
    elif len(unique) == 3:
        for x in unique:
            if dice.count(x) == 2:
                p = x
                unique.remove(p)
                break
        return unique[0] * unique[1]
    elif len(unique) == 4:
        return min(unique)
    
        
        
        
    
    
