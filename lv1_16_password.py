def solution(s, n):
    answer = ''
    for i in range(0, len(s)):
        temp = 0
        temp = ord(s[i])+n
        if s[i] == ' ':
            answer += s[i]
        elif s[i] >= 'a' and s[i] <='z':
            if temp > ord('z'):
                answer += chr(temp-26)
            else:
                answer += chr(temp)
        elif s[i] >= 'A' and s[i] <='Z':
            if temp > ord('Z'):
                answer += chr(temp-26)
            else:
                answer += chr(temp)            
    return answer

print(solution("AaZz",25))