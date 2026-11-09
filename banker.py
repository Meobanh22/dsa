def banker(available, max_demand, allocation):
    R = len(allocation[0])
    n = len(allocation)
    need = [[max_demand[i][j] - allocation[i][j] for j in range(R)] for i in range(n)]
    print(need)
    finish = [False] * n
    while True:
        left = False
        for k, P in enumerate(need):
            if not finish[k] and all(P[i] <= available[i] for i in range(R)):
                available = [available[i] + allocation[k][i] for i in range(R)]
                finish[k] = True
                left = True

                process = ["P" + str(i) for i in range(n)]
                finish_str = "   ".join("T" if f else "F" for f in finish)
                print()
                print("         " + "  ".join(process))
                print(f"Finish:  {finish_str}")
                print(f"Work:    {*available,}")
        if not left:
            break

banker([4, 5, 7, 1], [[3, 2, 2, 1], [4, 2, 2, 2], [3, 3, 3, 3]], [[0, 1, 0, 0], [2, 0, 0, 1], [3, 0, 2, 1]])