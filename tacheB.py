import properties


def DIST_1(x: str, y: str):
    N = len(x)
    M = len(y)
    T = []

    for i in range(0, N + 1):
        T.append([i * properties.c_del])
    for j in range(1, M + 1):
        T[0].append(j * properties.c_ins)

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            T[i].append(min([T[i][j - 1] + properties.c_ins,
                             T[i - 1][j] + properties.c_del, T[i - 1][j - 1] + properties.c_sub(x[i - 1], y[j - 1])]))

    return T[N][M]


if __name__ == "__main__":
    print("DIST_1('A', '') =", DIST_1("A", ""))  # renvoi 2
    print("DIST_1('A', 'B') =", DIST_1("A", "B"))  # renvoi 3

    print("DIST_1('ATCG', '') = ", DIST_1("ATCG", ""))  # renvoi 8
    print("DIST_1('', 'ATCG') = ", DIST_1("", "ATCG"))  # renvoi 8
    print("DIST_1('AB', 'CG') = ", DIST_1("AB", "CG"))  # renvoi 8
