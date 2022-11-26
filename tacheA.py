import math
import properties


def nb_align(n: int, m: int) -> int:
    """
    :param n: Taille d'un mot x
    :param m: Taille d'un mot y
    :return: Nombre d'alignement de (x,y)
    """
    nb_aligns = 0
    for k in range(0, m+1):
        nb_aligns = nb_aligns + math.comb(n+k, k)*math.comb(n, m-k)
    return nb_aligns


# Tache A

def DIST_NAIF_REC(x: str, y: str, i: int, j: int, c: float, dist: float) -> float:
    """
    :param x: mot
    :param y: mot
    :param i: indice parcourant x
    :param j: indice parcourant y
    :param c: coup de l'allignement pour (x_[1,...,i],y_[1,...,j])
    :param dist: le meilleur alignement de (x,y) connu avant l'appel
    :return: cout du meilleur alignement de (x,y) après l'appel
    """
    n = len(x) - 1  # dernier indice de x
    m = len(y) - 1  # dernier indice de y

    if i == n and j == m:  # Si on a parcourue tout x et y
        if c < dist:
            dist = c

    else:
        if i < n and j < m:
            dist = DIST_NAIF_REC(x, y, i + 1, j + 1, c + properties.c_sub(x[i + 1], y[j + 1]), dist)
        if i < n:
            dist = DIST_NAIF_REC(x, y, i + 1, j, c + properties.c_del, dist)
        if j < m:
            dist = DIST_NAIF_REC(x, y, i, j + 1, c + properties.c_ins, dist)

    return dist


def DIST_NAIF(x: str, y: str):
    """
    :param x: un mot
    :param y: un mot
    :return: distance entre x et y
    """
    return DIST_NAIF_REC(x, y, -1, -1, 0, math.inf)
