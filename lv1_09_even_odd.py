def solution(num):
    answer = ""
    if int(num % 2) == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer


num = 3
print(solution(num))

num = 4
print(solution(num))
