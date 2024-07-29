def solution(my_string):
    frequency = [0] * 52
    
    for letter in my_string:
        if 'A' <= letter <= 'Z':
            frequency[ord(letter) - ord('A')] += 1
        elif 'a' <= letter <= 'z':
            frequency[ord(letter) - ord('a') + 26] += 1
    
    return frequency