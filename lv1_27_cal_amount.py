def solution(price, money, count):
    answer = -1
    need_money = sum([price * m for m in range(1,count+1)])
    if need_money > money:
        answer = need_money - money
    else:
        answer = 0
    return answer

print(solution(3,20,4))