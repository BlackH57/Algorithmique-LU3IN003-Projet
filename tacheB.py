import properties


def TAB_DIST(x: str, y: str):
    """
    :param x: Un mot
    :param y: Un mot
    :return: Tableau contenant les D(i,j)
    """
    N = len(x)
    M = len(y)
    T = []

    for i in range(0, N + 1):               # On rempli la premiere colonne
        T.append([i * properties.c_del])
    for j in range(1, M + 1):               # On rempli la premiere ligne
        T[0].append(j * properties.c_ins)

    for i in range(1, N + 1):               # On rempli le reste
        for j in range(1, M + 1):
            T[i].append(min([T[i][j - 1] + properties.c_ins,
                             T[i - 1][j] + properties.c_del, T[i - 1][j - 1] + properties.c_sub(x[i - 1], y[j - 1])]))

    return T


def DIST_1(x: str, y: str):
    """
    :param x: Un mot
    :param y: Un mot
    :return: La distance d'edition entre x et y
    """
    N = len(x)
    M = len(y)
    T = TAB_DIST(x, y)

    return T[N][M]
# Ndt : Le code est un peu different du pseudo-code. Par soucis de lisibilite on calcule
#       le tableau dans une fonction a part

def SOL_1(x: str, y: str, T: list[list[float]]):
    """
    :param x: Un mot
    :param y: Un mot
    :param T: Un tableau contenant les distances D(i,j)
    :return: un alignement de cout minimal de (x,y)
    """

    a1 = ""  # Stockage de l'alignement
    a2 = ""

    i = len(x)  # Iterateur sur la taille des mots
    j = len(y)

    while i > 0 and j > 0:
        if T[i][j] == T[i][j - 1] + properties.c_ins:  # Identification du min
            j -= 1
            a1 = "-" + a1
            a2 = y[j] + a2

        elif T[i][j] == T[i - 1][j] + properties.c_del:  # Meme demarche
            i -= 1
            a1 = x[i] + a1
            a2 = "-" + a2
        else:  # Meme demarche
            i -= 1
            j -= 1
            a1 = x[i] + a1
            a2 = y[j] + a2

    if i > 0:  # S'il reste des lettres de x non utilisees (et pas pour y)
        gps = ""
        for n in range(i):
            gps += "-"
        return x[0:i] + a1, gps + a2
    if j > 0:  # S'il reste des lettres de y non utilisees (et pas pour x)
        gps = ""
        for n in range(i):
            gps += "-"
        return gps + a1, y[0:j] + a2

    return a1, a2  # Si toutes les lettres ont ete utilisees


def PROG_DYN(x: str, y: str):
    """
    :param x: Un mot
    :param y: Un mot
    :return: La distance d'edition et un alignement de cout minimale
    """
    T = TAB_DIST(x, y)
    return T[len(x)][len(y)], SOL_1(x, y, T)


if __name__ == "__main__":
    print("============= Test DIST_1 =============")
    print("DIST_1('A', '') =", DIST_1("A", ""))  # renvoi 2
    print("DIST_1('A', 'C') =", DIST_1("A", "C"))  # renvoi 3
    print("DIST_1('ATCG', '') = ", DIST_1("ATCG", ""))  # renvoi 8
    print("DIST_1('', 'ATCG') = ", DIST_1("", "ATCG"))  # renvoi 8
    print("DIST_1('AT', 'CG') = ", DIST_1("AT", "CG"))  # renvoi 8
    print("DIST_1('ATTGTA', 'ATCTTA') =", DIST_1("ATTGTA", "ATCTTA"))  # renvoi 4
    print("============= Fin Test =============")

    print("============= Test SOL_1 =============")
    print("SOL_1('ATCG', 'ATCG') =", SOL_1("ATCG", "ATCG", TAB_DIST("ATCG", "ATCG")))
    print("SOL_1('AT', 'CG') =", SOL_1("AT", "CG", TAB_DIST("AT", "CG")))
    print("SOL_1('ATTGTA', 'ATCTTA') =", SOL_1("ATTGTA", "ATCTTA", TAB_DIST("ATTGTA", "ATCTTA")))
    print("============= Fin Test =============")

    print("============= Test PROG_DYN =============")
    print("PROG_DYN('ATTGTA', 'ATCTTA') =", PROG_DYN("ATTGTA", "ATCTTA"))
    print("PROG_DYN('AT', 'CG') =", PROG_DYN("AT", "CG"))
    print("============= Fin Test =============")
