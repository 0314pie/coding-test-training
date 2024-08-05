def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    l = len(pat)
    
    for a in range(len(myString) - l + 1):
        if myString[a: a + l] == pat:
            return 1
    
    return 0