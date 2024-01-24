def solution(array, commands):
    blank = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        sarr = array[i-1:j]
        blank.append(sorted(sarr)[k-1])     
    return blank

            
            
    
  