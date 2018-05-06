def solution(s):
    var = s.lower()
    p_num = 0
    y_num = 0
    for i in range(len(var)):
        if var[i] == 'p':
            p_num += 1
        elif var[i] == 'y':
            y_num += 1

    if p_num == y_num:
        return True
    else:
        return False

print(solution('PpooasdfayY'))
print(solution(''))
print(solution('PYy'))