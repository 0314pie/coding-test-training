def solution(myStr):
    split_str = myStr.split('a')
    split_str = [item for part in split_str for item in part.split('b')]
    split_str = [item for part in split_str for item in part.split('c')]
    
    result = [s for s in split_str if s]
    
    if not result:
        return ["EMPTY"]
    
    return result