import enum


def solution(phone_number):
    answer = ""
    length = len(phone_number)
    for i, number in enumerate(phone_number):
        if i < length - 4:
            answer += "*"
        else:
            answer += number
    return answer


print(solution("01033334444"))
print(solution("027778888"))
