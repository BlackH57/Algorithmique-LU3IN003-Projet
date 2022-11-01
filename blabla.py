import math
import time
from cmath import inf

import properties
import tools


def nb_align(n: int, m: int) -> int:
    """
    Prend en entré la taille de deux mots x et y
    Retourne le nombre d'allignement possible
    """
    nb_aligns = 0
    for k in range(n - m, m):
        nb_aligns = nb_aligns + math.comb(n, m - k) * ((n + 1) ** k)
    return nb_aligns


# Tache A

def DIST_NAIF_REC_1(x: str, y: str, i: int, j: int, c: float, dist: float):
    if i == len(x) - 1 and j == len(y) - 1:
        if c < dist:
            dist = c

    else:
        if i < len(x) - 1 and j < len(y) - 1:
            if x[i + 1] not in {' ', '\n'} and y[j + 1] not in {' ', '\n'}:
                if x[i + 1] == y[j + 1]:
                    dist = DIST_NAIF_REC_1(x, y, i + 1, j + 1, c, dist)
                else:
                    if (x[i + 1] in {'A', 'T'} and y[j + 1] in {'A', 'T'}) or (
                            x[i + 1] in {'G', 'C'} and y[j + 1] in {'G', 'C'}):
                        dist = DIST_NAIF_REC_1(x, y, i + 1, j + 1, c + 3, dist)
                    else:
                        dist = DIST_NAIF_REC_1(x, y, i + 1, j + 1, c + 4, dist)
            else:
                dist = DIST_NAIF_REC_1(x, y, i + 1, j + 1, c, dist)
        if i < len(x) - 1:
            if x[i + 1] not in {' ', '\n'}:
                dist = DIST_NAIF_REC_1(x, y, i + 1, j, c + properties.c_del, dist)
            else:
                dist = DIST_NAIF_REC_1(x, y, i + 1, j, c, dist)
        if j < len(y) - 1:
            if y[j + 1] not in {' ', '\n'}:
                dist = DIST_NAIF_REC_1(x, y, i, j + 1, c + properties.c_ins, dist)
            else:
                dist = DIST_NAIF_REC_1(x, y, i, j + 1, c, dist)
    return dist


def DIST_NAIF_1(x, y):
    return DIST_NAIF_REC_1(x, y, -1, -1, 0, inf)


def DIST_NAIF_REC_2(x: str, y: str, i: int, j: int, c: float, dist: float) -> float:
    """
    :param x: mot
    :param y: mot
    :param i: indice parcourant x
    :param j: indice parcourant y
    :param c: coup de l'allignement pour (x_[1,...,i],y_[1,...,j])
    :param dist: le meilleur alignement de (x,y) connu avant l'appel
    :return: coup du meilleur alignement de (x,y) après l'appel
    """
    n = len(x) - 1  # dernier indice de x
    m = len(y) - 1  # dernier indice de y
    if i == n and j == m:  # Si on a parcourue tout x et y
        if c < dist:
            dist = c

    else:
        if i < n and j < m:
            dist = DIST_NAIF_REC_2(x, y, i + 1, j + 1, c + properties.c_sub(x[i + 1], y[j + 1]), dist)
        if i < n:
            dist = DIST_NAIF_REC_2(x, y, i + 1, j, c + properties.c_del, dist)
        if j < m:
            dist = DIST_NAIF_REC_2(x, y, i, j + 1, c + properties.c_ins, dist)

    return dist


def DIST_NAIF_2(x: str, y: str):
    """
    :param x: un mot
    :param y: un mot
    :return: distance entre x et y
    """
    return DIST_NAIF_REC_2(x, y, 0, 0, 0, math.inf)


# _________________________________________________________________
def main():
    f = open("Instances_genome/Inst_0000010_7.adn", 'r')
    # 12_56 : 62.93026399612427 s
    n = f.readline()
    m = f.readline()
    x = tools.del_space(f.readline())
    y = tools.del_space(f.readline())
    print("x: " + x, "y: " + y)

    # print(x,len(x))
    # print(y,len(y))
    f.close()

    start = time.time()
    print(DIST_NAIF_2(x, y))
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
