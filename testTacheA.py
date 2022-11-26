import tacheA
import tools


def nb_align_test(n: int, m: int):
    res, time_used, memory_used = tools.func_profil(tacheA.nb_align, n, m)
    print("Nb alignement pour n = ", n, " et m = ", m, " : ", res)
    print("nombre alignement : \t", res)
    print("temps d'execution : ", time_used)
    print("memoire utilisee : ", memory_used / (1024.0 ** 1), "kB")


def dist_naif_test(x: str, y: str, n=None, m=None):
    res, time_used, memory_used = tools.func_profil(tacheA.DIST_NAIF, x, y)
    if n is None:
        n = len(x)
    if m is None:
        m = len(y)
    print("x: " + x + "\ttaille: ", n)
    print("y: " + y + "\ttaille: ", m)
    print("distance : \t", res)
    print("temps d'execution :", time_used)
    print("memoire utilisee : ", memory_used / (1024.0 ** 1), "kB")


def dist_naif_test_genome(path: str):
    (x, n), (y, m) = tools.get_genome(path)
    dist_naif_test(x, y, n, m)


def test_nb_align():
    print("======== Calcul de nombre d'alignement ========")
    print("TEST 1 :")
    nb_align_test(0, 10)
    print()

    print("TEST 2 :")
    nb_align_test(10, 0)
    print()

    print("TEST 3 :")
    nb_align_test(15, 10)
    print()
    print("======== Fin Test nb_align ========")


def test_dist_naif():
    print("======== Test DIST_NAIF ========")
    print("TEST 1 :")
    dist_naif_test("A", "")         # renvoi 3
    print()

    print("TEST 2:")
    dist_naif_test("A", "B")        # renvoi 4
    print()

    print("TEST 3:")
    dist_naif_test("ATCG", "")      # renvoi 8
    print()

    print("TEST 4:")
    dist_naif_test("", "ATCG")      # renvoi 8
    print()

    print("TEST 5:")
    dist_naif_test("AB", "CG")      # renvoi 8
    print()

    print("TEST 6:")
    dist_naif_test("ATTGTA", "ATCTTA")    # renvoi 4
    print("======== Fin Test DIST_NAIF ========")


def test_dist_naif_genomes():
    print("============== Test distance naive pour Inst_0000010_44 ==============")
    dist_naif_test_genome("Instances_genome/Inst_0000010_44.adn")

    print("============== Test distance naive pour Inst_0000010_7 ==============")
    dist_naif_test_genome("Instances_genome/Inst_0000010_7.adn")

    print("============== Test distance naive pour Inst_0000010_8.adn ==============")
    dist_naif_test_genome("Instances_genome/Inst_0000010_8.adn")

    print("============== Test distance naive pour Inst_0000012_56.adn ==============")
    dist_naif_test_genome("Instances_genome/Inst_0000012_56.adn")
    print("============== Fin Tests ==============")


if __name__ == "__main__":
    test_nb_align()
    test_dist_naif()
    test_dist_naif_genomes()
