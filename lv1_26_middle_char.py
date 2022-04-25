def solution(s):
    answer = ''
    length = len(s)
    if length%2 !=0:
        answer = s[length//2]
    else:
        idx = length//2
        answer = s[idx-1:idx+1]
    return answer

print(solution("abcde"))
print(solution("qwer"))