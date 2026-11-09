import random

def hanoi_solver(n):
    A = list(range(n, 0, -1))
    B = []
    C = []
    def move(n, source, target, auxiliary):
        if n == 1:
            target.append(source.pop())
            return
        move(n - 1, source, auxiliary, target)
        print(f"{A} {B} {C}")
        target.append(source.pop())
        print(f"{A} {B} {C}")
        move(n - 1, auxiliary, target, source)
    move(n, A, C, B)

n = random.randint(1, 8)
print(f"Number of disks: {n}")
hanoi_solver(n)