def solution(s):
    if len(s) % 2 == 0:
        index_num = len(s) // 2
        return s[index_num-1:index_num+1]
    else:
        index_num = (len(s) // 2) + 1
        return s[index_num-1]