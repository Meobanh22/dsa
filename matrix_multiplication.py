import random

def multiplication(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

n = random.randint(1, 8)
mA = random.randint(1, 8)
mB = random.randint(1, 8)
A = list(random.sample(range(1, 10), n) for _ in range(mA))
B = list(random.sample(range(1, 10), mB) for _ in range(n))
multiplication_result = multiplication(A,B)
print(f"Matrix A({n}x{mA}):")
for row in A:
    print(*row)
print(f"\nMatrix B({mB}x{n}):")
for row in B:
    print(*row)
print(f"\nMultiplication Result({mA}x{mB}):")
for row in multiplication_result:
    print(*row)