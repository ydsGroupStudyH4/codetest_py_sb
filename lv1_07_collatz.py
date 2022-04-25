def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        answer += 1
        if num == 1:
            break
        elif answer >= 500:
            answer = -1
            break
    return answer


num = 6
print(solution(num))

num = 16
print(solution(num))

num = 626331
print(solution(num))
