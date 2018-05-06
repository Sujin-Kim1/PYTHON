rank = {
    "JTJ" : 100,
    "KKK" : 10,
    "KWQD" : 12,
    "dkkjkkk" : 123123,
    "SJ" : -99999,
    "PPPPP" : 123
}

# 숫자 가장 높은 사람은?

a = []
for k, v in rank.items():
    a.append((k,v))
    a.sort(key = lambda x : x[1], reverse = True)
print(a[0][0])
