def soulution(arr):
    arr.sort()
    li = []
    for i in range (len(arr)):
        li.append(i+1)
    if li == arr:
        return True
    else:
        return False


print(soulution([1,3,3,4,5]))

