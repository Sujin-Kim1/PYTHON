def sum_func(n):
    n = str(n)
    answer = 0
    for i in range(len(n)):
        answer += int(n[i])

    return answer

print('sum = ', sum_func(13534))