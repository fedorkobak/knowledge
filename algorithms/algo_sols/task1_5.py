from math import ceil

def sol(K1, M, K2, P2, N2):
    
    if N2 > M:
        return (-1, -1)

    T2 = M*(P2 - 1) + N2
    
    if T2 > K2:
        return (-1, -1)

    P1 = 0
    N1 = 0

    if T2 > 1:
        G = ceil(K2/T2)

        if (T2-1)*G >= K2:
            return (-1, -1)

        T1 = ceil(K1/G)
        P1 = ceil(T1/M)
        N1 = T1 - (P1-1)*M
    elif K1 <= K2:
        N1 = N2; P1 = P2
    elif M == 1:
        N1 = 1

    return P1, N1

if __name__ == "__main__":
    print(" ".join(map(str,
        sol(*map(int, input().split(" ")))
    )))