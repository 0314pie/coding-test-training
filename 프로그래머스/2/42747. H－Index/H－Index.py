def solution(citations):
    b = [] 
    
    citations.sort(reverse=True)
    for a in range(len(citations)):
        if a+1 > citations[a]:
            answer = a
            break
        else: answer = (len(citations))
        
        
    return answer
