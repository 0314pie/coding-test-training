def solution(array):
    # 각 값의 빈도를 저장할 딕셔너리
    count_dict = {}
    
    # 배열 순회하며 빈도수 계산
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # 최빈값 찾기
    max_count = 0
    modes = []
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            modes = [num]
        elif count == max_count:
            modes.append(num)
    
    # 최빈값이 여러 개인지 확인하고 반환
    if len(modes) == 1:
        return modes[0]
    else:
        return -1
