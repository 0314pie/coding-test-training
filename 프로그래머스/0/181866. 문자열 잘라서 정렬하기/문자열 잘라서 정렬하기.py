def solution(myString):
    result = myString.split("x")
    result = [s for s in result if s]
    return sorted(result)


    