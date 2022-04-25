def solution(arr1, arr2):
    answer = [[]]
    row = len(arr1)
    col = len(arr1[0])
    answer = [[0] * col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            answer[r][c] = arr1[r][c] + arr2[r][c]
    return answer


arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))


arr1 = [[1], [2]]
arr2 = [[3], [4]]

print(solution(arr1, arr2))
