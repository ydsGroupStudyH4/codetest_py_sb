def solution(n, m):
    answer = []
    _max, _min = max(n, m), min(n, m)
    while _min:
        _max, _min = _min, _max % _min
        print(_max, _min)
    answer = [_max, int(n * m / _max)]

    # # gdc
    # gdc = get_gdc(n, m)
    # answer.append(gdc)
    # # lcm
    # lcm = get_lcm(n, m)
    # answer.append(lcm)
    return answer


def get_gdc(n, m):
    dc_n_set = set(get_dc(n, n))
    dc_m_set = set(get_dc(m, n))
    dc_set = dc_n_set.intersection(dc_m_set)
    return max(dc_m_set)


def get_dc(number, range_number):
    dc_list = [dc for dc in range(1, range_number + 1) if number % dc == 0]
    return dc_list


def get_lcm(n, m):
    cm_n_set = set(get_cm(n, m))
    cm_m_set = set(get_cm(m, n))
    cm_set = cm_n_set.intersection(cm_m_set)
    return min(cm_set)


def get_cm(number, range_number):
    cm_list = [number * i for i in range(1, range_number + 1)]
    return cm_list


n = 3
m = 12
print(solution(n, m))

n = 2
m = 5
print(solution(n, m))


n = 3
m = 5
print(solution(n, m))
