import random
from math import comb

def C(n, k):
    i =  n - k
    res = 1
    for j in range(n, 1, -1):
        if j > k:
            res *= j
        if j <= i:
            res//= j
    return res

n = random.randint(1, 100)
k = random.randint(1, n)
print(f"n: {n}\nk: {k}\nC(n, k): {C(n, k)}")
if comb(n, k) == C(n, k):
    print("The result is correct.")
else:
    print("The result is incorrect.")   