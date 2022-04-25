def solution(seoul):
    answer = ''
    find_name = "Kim"
    answer = str.format(f"김서방은 {seoul.index(find_name)}에 있다")
    return answer

seoul = ["Jane", "Kim"]
print(solution(seoul))