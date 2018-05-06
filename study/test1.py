def expressions(num):
    answer = 0
    cursor = 1
    plus = 0
    total = 0
    while (cursor <= num):
        while (total < num):
            total += cursor + plus
            print('total : ', total)
            plus += 1
            print("plus : ", plus)
        if total >= num:
            if total == num:
                answer += 1
                print("answer : ", answer)
            total = 0
            plus = 0

        cursor += 1
        print("cursor : ", cursor)


    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
