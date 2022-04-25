def solution(s):
    answer = True
    if s.isdigit() and len(s) == 4 or len(s) == 6:
        pass
    else:
        answer = False
    return answer

print(solution("a234"))
print(solution("1234"))