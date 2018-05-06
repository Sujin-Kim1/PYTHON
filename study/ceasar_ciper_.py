def caesar(s, n):
    result = ""
    li = []
    n = int(n % 26)
    for i in s:
        li.append(i)
    for j in li:
        if ord("A") <= ord(j) <= ord("Z"):
            if ord(j) + n > ord('Z'):
                j = chr(ord(j) + n - 26)
            else:
                j = chr(ord(j) + n)

        elif ord('a') <= ord(j) <= ord('z'):
            if ord(j) + n > ord('z'):
                j = chr(ord(j) + n - 26)
            else:
                j = chr(ord(j) + n)

        result += j

    return result

# 65~90 A~Z  97~122 a~z
# 주어진 문장을 암호화하여 반환하세요.
# 실행을 위한 테스트코드입니다.

print('s는 "a B z", n은 4인 경우: ' + '\"' + caesar("a B z", 4) + '\"')

