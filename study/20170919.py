# a = [5, 4, 7, 4, 9, 6, 2]
# for x in enumerate(a):
import time
import random
numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]
ts = time.time()
newnbrs = sorted(numbers)
ts = time.time() - ts
print("Built-In", numofnbrs, "elapsed time =", ts)