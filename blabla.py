import math
import time
import tools
import properties


def nb_align(n: int, m: int) -> int:
    """
    :param n: Taille d'un mot x
    :param m: Taille d'un mot y
    :return: Nombre d'alignement de (x,y)
    """
    nb_aligns = 0
    for k in range(n - m, m):
        nb_aligns = nb_aligns + math.comb(n, m - k) * ((n + 1) ** k)
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
    :return: coup du meilleur alignement de (x,y) après l'appel
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


def file_dist_naif_test(path: str):
    """
    Affiche dans le terminale les mots, leurs longueurs, la distance et le temps mis en utilisant DIST_NAID
    :param path: Chemin de repertoire courant au fichier que l'on souhaite lire
    :return: None
    """
    # ouverture du fichier
    file = open(path, 'r')

    # on passe les deux premieres lignes
    n = tools.del_space(file.readline())
    m = tools.del_space(file.readline())

    # on stock les deux mots
    x = tools.del_space(file.readline())
    y = tools.del_space(file.readline())

    # affichage des deux mots
    print("x:" + x + "\ttaille : " + n)
    print("y:" + y + "\ttaille : " + m)

    # fermeture du fichier
    file.close()

    # Debut du chrono
    start = time.time()

    dist = DIST_NAIF(x, y)
    print("Distance entre x et y : ", dist)

    # Fin du chrono
    end = time.time()

    print("temps d'execution : ", end - start)

    # 12_56 : 62.93026399612427 s


def main():
    print("============== Test distance naive pour Inst_0000010_44 ==============")
    file_dist_naif_test("Instances_genome/Inst_0000010_44.adn")
    print("============== Fin Test ==============")
    print("============== Test distance naive pour Inst_0000010_7 ==============")
    file_dist_naif_test("Instances_genome/Inst_0000010_7.adn")
    print("============== Fin Test ==============")
    print("============== Test distance naive pour Inst_0000010_8.adn ==============")
    file_dist_naif_test("Instances_genome/Inst_0000010_8.adn")
    print("============== Fin Test ==============")


if __name__ == "__main__":
    main()
