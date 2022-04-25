def solution(n):
    answer = 0
    number_list = []
    recursive_div_ten(number_list, n)
    number_list.sort(reverse=True)
    string_number = "".join(map(str, number_list))
    return int(string_number)


def recursive_div_ten(number_list, number):
    if number < 10:
        number_list.append(number)
        return
    sol, remd = divmod(number, 10)
    number_list.append(remd)
    recursive_div_ten(number_list, sol)
    return


print(solution(118372))
