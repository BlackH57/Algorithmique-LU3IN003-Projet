c_del = 2
c_ins = 2
alphabet = {"A", "T", "G", "C"}
concordant = [["A", "T"], ["G", "C"]]


def c_sub(a: str, b: str) -> int:
    """
    :param a: caractere
    :param b: caractere
    :return: cout de soustraction entre a et b
    """
    if a == b:
        return 0
    if {a, b} == {"A", "B"} or {a, b} == {"C", "G"}:
        return 3

    return 4


def cost_list_sub():
    return [c_sub(concordant[0][0], concordant[0][0]),
            c_sub(concordant[1][0], concordant[1][0]),
            c_sub(concordant[1][0], concordant[0][0]),
            c_sub(concordant[0][0], concordant[1][0])
            ]


def cost_list():
    """
    :return: Une liste des couts possible
    """
    return [c_del, c_ins] + cost_list_sub()


def min_cost_sub():
    return min(cost_list_sub())


def min_cost():
    """
    :return: Le cout minimum des cout possibles
    """
    return min(cost_list())



"""
c_del = 3
c_ins = 3
consomnes = {"B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"}
voyelles = {"A", "E", "I", "O", "U", "Y"}


def c_sub(a: str, b: str) -> int:
    
    Utilise pour la question 23 du sujet
    :param a: Un caractere
    :param b: Un caractere
    :return: Cout de soustraction entre a et b
    
    if a == b:
        return 0
    if (a in voyelles and b in voyelles) or (a in consomnes and b in consomnes):
        return 5

    return 7
"""
