def solution(myString, pat):
    transformed = myString.replace("A", "X").replace("B", "A").replace("X", "B")
    
    if pat in transformed:
        return 1
    else:
        return 0