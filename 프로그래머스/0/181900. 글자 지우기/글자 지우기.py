def solution(my_string, indices):
    string = list(my_string)

    for i in indices:
        string[i] = "" 

    return "".join(string)