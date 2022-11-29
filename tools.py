import os
import time
import tracemalloc

import matplotlib.pyplot as plt


def del_space(x: str) -> str:
    """
    :param x: mot dont on veut enlever les espaces
    :return: x sans les espaces
    """
    acc = ""
    for c in x:
        if c not in [" ", "\n"]:
            acc += c
    return acc


def get_genome(path: str):
    """
    On recupere les genomes x et y contenus dans path
    :param path: Le chemin vers le génome
    :return: (x, |x|), (y, |y|)
    """

    genome = open(path, 'r')

    n = int(genome.readline())
    m = int(genome.readline())
    x = del_space(genome.readline())
    y = del_space(genome.readline())
    genome.close()

    return (x, n), (y, m)


def func_profil(func, *args, **kwargs):
    """
    :param func: Une fonction
    :param args: Les arguments de la fonction
    :param kwargs: Les arguments de la fonction
    :return: resultat de l'appel, le temps utilise
    """
    start = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start

    return result, elapsed_time


def memory_time_consumption(func, allowed_time=10):
    """
    :param func: Fonction dont on doit tester les performances
    :param allowed_time: Nombre de minutes maximum pour une instance
    :return: Une liste du temps et de la mémoire utilisé en fonction de la taille du premier mot.
    """
    n_t_m = []
    filenames = sorted(os.listdir("Instances_genome"))
    tracemalloc.start()

    for filename in filenames:
        (x, n), (y, m) = get_genome("".join(("Instances_genome/", filename)))
        _, time_used = func_profil(func, x, y)
        mem_used, peak = tracemalloc.get_traced_memory()
        tracemalloc.clear_traces()

        n_t_m.append((n, time_used, peak))
        print("genome:{name} n:{taille}\t time:{t}\tmemory:{m}".format(name=filename, taille=n, t=time_used, m=peak))

        if time_used > allowed_time * 60:
            break

    return n_t_m


def write_info_list(lf, func):
    """
    :param lf: Liste contenant des informations sur une fonction
    :param func: fonction tester
    :return: None
    """
    name = "".join(("memory_and_time/", func.__name__, ".txt"))
    fic = open(name, "w")
    for tpl in lf:
        fic.write("{n}\t{t}\t{m}\n".format(n=tpl[0], t=tpl[1], m=tpl[2]))
    fic.close()


def read_info_list(path):
    """
    :param path: Emplacement du fichier
    :return: Une liste contenant les informations du fichier
    """
    fic = open(path)
    lines = fic.readlines()
    lf = []
    for line in lines:
        n, t, m = line.split()
        lf.append((float(n), float(t), float(m)))

    return lf


def plot_information_from_fic(path, mode, name=""):
    """
    :param name: Nom de la fonction
    :param path: fichier contenant les informations d'une fonction
    :param mode: Si mode=0 affiche le temps, si mode=1 affiche la memoire
    :return: None
    """
    if mode not in [0, 1]:
        return

    lf = read_info_list(path)

    if mode == 0:
        name_mode = "time"
    else:
        name_mode = "memory"

    plt.plot([tpl[0] for tpl in lf], [tpl[mode + 1] for tpl in lf])

    plt.suptitle("".join((name, " ", name_mode)))
    plt.xlabel("taille du premier mot")
    if mode == 0:
        plt.ylabel("time (seconde)")
    else:
        plt.ylabel("memory (byte)")
    plt.show()


def plot_information_from_list(lf, mode, name=""):
    """
    :param name: Nom de la fonction
    :param lf: liste contenant les informations d'une fonction
    :param mode: Si mode=0 affiche le temps, si mode=1 affiche la memoire
    :return: None
    """
    if mode not in [0, 1]:
        return

    if mode == 0:
        name_mode = "time"
    else:
        name_mode = "memory"

    plt.plot([tpl[0] for tpl in lf], [tpl[mode + 1] for tpl in lf])
    plt.suptitle("".join((name, " ", name_mode)))
    plt.xlabel("taille du premier mot")
    if mode == 0:
        plt.ylabel("time (seconde)")
    else:
        plt.ylabel("memory (byte)")
    plt.show()
