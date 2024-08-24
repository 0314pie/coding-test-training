def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    num = 1  
    row, col = 0, 0  
    right, down, left, up = 0, n - 1, n - 1, 0  
    
    while num <= n**2:
        for col in range(right, down + 1):
            answer[row][col] = num
            num += 1
        right += 1  
        row += 1  
        
        for row in range(right, left + 1):
            answer[row][down] = num
            num += 1
        down -= 1 
        col -= 1  

        for col in range(down, up - 1, -1):
            answer[left][col] = num
            num += 1
        left -= 1 
        row -= 1 
        

        for row in range(left, right - 1, -1):
            answer[row][up] = num
            num += 1
        up += 1  
        col += 1  
    
    return answer
