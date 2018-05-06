def no_continuous(s):
    answer = []
    for i in range(len(s)):
        if not s[i] in answer:
            answer += s[i]
    return answer

print(no_continuous('asd gdsdf 313'))