import properties


def DIST_2(x: str, y: str):
    """

    :param x: Un mot
    :param y: Un mot
    :return: Distance d'edition entre x et y
    """

    N = len(x)
    M = len(y)

    T = [[], []]    # Stock les distances

    for j in range(0, M+1):
        (T[0]).append(j*properties.c_ins)
    T[1] = [0 for i in range(0, M+1)]       # On veut eviter les effet de bords

    for i in range(1, N+1):
        T[1][0] = i*properties.c_del
        for j in range(1, M+1):
            T[1][j] = min([T[1][j-1] + properties.c_ins,
                           T[0][j] + properties.c_del,
                           T[0][j-1] + properties.c_sub(x[i-1], y[j-1])])
        T[0] = [c for c in T[1]]        # On veut eviter les effet de bords

    return T[0][M]


if __name__ == "__main__":

    print("============= Test DIST_1 =============")
    print("DIST_1('A', '') =", DIST_2("A", ""))  # renvoi 2
    print("DIST_1('A', 'C') =", DIST_2("A", "C"))  # renvoi 4
    print("DIST_1('ATCG', '') = ", DIST_2("ATCG", ""))  # renvoi 8
    print("DIST_1('', 'ATCG') = ", DIST_2("", "ATCG"))  # renvoi 8
    print("DIST_1('AT', 'CG') = ", DIST_2("AT", "CG"))  # renvoi 8

    print("DIST_1('ATTGTA', 'ATCTTA') =", DIST_2("ATTGTA", "ATCTTA"))  # renvoi 4
    print("============= Fin Test =============")
