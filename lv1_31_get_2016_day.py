def solution(a, b):
    answer = ""
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    delta_month = a - 1
    delta_day = b - 1
    month_to_day = 0
    for i in range(delta_month):
        if i == 1:
            month_to_day += 29
        elif ((i + 1) <= 7 and (i + 1) % 2 == 1) or ((i + 1) >= 8 and (i + 1) % 2 == 0):
            month_to_day += 31
        elif ((i + 1) <= 7 and (i + 1) % 2 == 0) or ((i + 1) >= 8 and (i + 1) % 2 == 1):
            month_to_day += 30
    answer = days[(5 + month_to_day + delta_day) % 7]
    return answer


print(solution(5, 24))
