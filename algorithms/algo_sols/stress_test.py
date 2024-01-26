import numpy as np
from math import ceil
from task1_5 import sol
from task1_5_official_sol import slow

while True:
    K1, M, K2, P2, N2 = np.random.randint(1, 1000, 5)

    T2 = M*(P2-1) + N2

    if (N2 > M) or (T2 > K2):
        continue

    my_solution = sol(K1, M, K2, P2, N2)
    yandex_solution = slow(K1, M, K2, P2, N2)
    print((K1, M, K2, P2, N2))
    print("My solution", my_solution)
    print("Yandex solution", yandex_solution)
    if not my_solution == yandex_solution:
        break