def solution(my_string, is_suffix):
    l = len(my_string) - len(is_suffix) 
    if l < 0:
        return 0
    elif my_string[l:] == is_suffix:
        return 1
    else: return 0