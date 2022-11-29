import properties
import math


def mot_gapes(n: int):
    """
    :param n: Une taille
    :return: Le mot constitue de n gapes
    """
    return n * "-"


def align_lettre_mot(x, y):
    """
    :param x: Une lettre
    :param y: Un mot
    :return: Alignement minimale de (x,y)
    """
    N = len(y)
    m_gap = mot_gapes(N)
    c_min = math.inf    # Majoration du cout
    i_min = -1          # indice du cout min
    min_cost_sub = properties.min_cost_sub()    # Cout minimal trouvable en echangeant un gap par x

    for i in range(0, N):
        cost = properties.c_sub(x, y[i])
        if cost < c_min:    # Actualisation du min
            c_min = cost
            i_min = i
            if cost == min_cost_sub:    # Si on est dans ce cas il n y a plus d'amelioration possible
                break

    if c_min - properties.c_ins > properties.c_del:
        return "".join((x, m_gap)), "".join(("-", y))

    return "".join((m_gap[:i_min], x, m_gap[i_min + 1:])), y


def coupure(x, y):
    """
    :param x: Un mot
    :param y: Un mot
    :return: le rang de la lettre a laquelle on doit couper y.
    """
    N = len(x)
    M = len(y)

    T = [[], []]  # Stock les distances
    c_li = [[], []]  # Stock la colonne d'origine sur la ligne i

    for j in range(0, M + 1):
        (T[0]).append(j * properties.c_ins)  # Initialisation
        (T[1]).append(-1)  # Remplissage

        (c_li[0]).append(j)  # Initialisation
        (c_li[1]).append(-1)  # Remplissage

    for i in range(1, N // 2 + 1):
        T[1][0] = i * properties.c_del
        for j in range(1, M + 1):
            T[1][j] = min([T[1][j - 1] + properties.c_ins,
                           T[0][j] + properties.c_del,
                           T[0][j - 1] + properties.c_sub(x[i - 1], y[j - 1])])
        T[0] = [c for c in T[1]]  # On veut eviter les effet de bords

    # On separe la boucle en deux pour eviter les tests et le stockage a chaque iteration.

    for i in range(N // 2 + 1, N + 1):
        T[1][0] = i * properties.c_del
        for j in range(1, M + 1):
            # Calcul D(i,j)
            v1 = T[1][j - 1] + properties.c_ins
            v2 = T[0][j] + properties.c_del
            v3 = T[0][j - 1] + properties.c_sub(x[i - 1], y[j - 1])
            T[1][j] = min([v1, v2, v3])

            # Passage de la colonne d'origine
            if T[1][j] == v1:
                c_li[1][j] = c_li[1][j - 1]
            if T[1][j] == v2:
                c_li[1][j] = c_li[0][j]
            if T[1][j] == v3:
                c_li[1][j] = c_li[0][j - 1]

        T[0] = [c for c in T[1]]  # On veut eviter les effets de bords
        c_li[0] = [c for c in c_li[1]]

    return c_li[0][M]


def SOL_2(x: str, y: str):
    """
    :param x: Un mot
    :param y: Un mot
    :return: Un alignement de cout minimal
    """
    M = len(y)  # Stockage des tailles des mots
    N = len(x)

    # Traitement des cas de bases
    if N == 0:
        return mot_gapes(len(y)), y
    if M == 0:
        return x, mot_gapes(len(x))
    if N == 1:
        return align_lettre_mot(x, y)
    if M == 1:
        couple = align_lettre_mot(y, x)
        return couple[1], couple[0]

    i = N//2            # On recupere les indices de coupes
    j = coupure(x, y)

    a1 = SOL_2(x[:i], y[:j])    # Alignements des parties gauches
    a2 = SOL_2(x[i:], y[j:])    # Alignements des parties droites

    sol = "".join((a1[0], a2[0])), "".join((a1[1], a2[1]))
    return sol
