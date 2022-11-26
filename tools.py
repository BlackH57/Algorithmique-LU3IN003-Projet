import time
import psutil
import os


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

    return (x, n), (y, m)


def elapsed_since(start):
    """
    :param start: temps de depart 
    :return: temps ecoule depuis start.
    """
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))


def get_process_memory():
    """
    :return: Le memoire utiliser au moment de l'appel
    """
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def func_profil(func, *args, **kwargs):
    """
    :param func: Une fonction
    :param args: Les arguments de la fonction
    :param kwargs: Les arguments de la fonction
    :return: resultat de l'appel, le temps ecoule, la memoire utilisee en bit
    """
    mem_before = get_process_memory()
    start = time.time()
    result = func(*args, **kwargs)
    elapsed_time = elapsed_since(start)
    mem_after = get_process_memory()

    return result, elapsed_time, mem_after - mem_before
