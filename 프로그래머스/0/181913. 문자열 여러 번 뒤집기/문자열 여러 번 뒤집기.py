def solution(my_string, queries):
    for query in queries:
        s = int(query[0])
        e = int(query[1])
        reversed_string = my_string[s:e+1][::-1]
        my_string = my_string[:s] + reversed_string + my_string[e+1:]
    
    return my_string