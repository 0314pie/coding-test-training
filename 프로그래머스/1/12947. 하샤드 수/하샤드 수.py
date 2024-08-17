def solution(x):
    num_list = list(map(int, str(x)))  
    if x % sum(num_list) == 0:
        return True
    else:
        return False