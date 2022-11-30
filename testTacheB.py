import tacheB
import tools


def tab_dist_test(x: str, y: str):
    _, time_used, memory_used = tools.func_profil(tacheB.TAB_DIST, x, y)
    print("Temps d'execution : ", time_used)


def dist_1_test(x: str, y: str):
    res, time_used = tools.func_profil(tacheB.DIST_1, x, y)
    print("x: " + x + "\ttaille: ", len(x))
    print("y: " + y + "\ttaille: ", len(y))
    print("Distance d'edition entre x et y : \t", res)
    print("Temps d'execution : ", time_used)


def prog_dyn_test(x: str, y: str, n=None, m=None):
    res, time_used = tools.func_profil(tacheB.PROG_DYN, x, y)

    if n is None:
        n = len(x)
    if m is None:
        m = len(y)

    print("x: " + x + "\ttaille: ", n)
    print("y: " + y + "\ttaille: ", m)
    print("Alignement minimal de (x,y) : \t", res[1])
    print("Distance d'edition : ", res[0])
    print("Temps d'execution : ", time_used)


def prog_dyn_test_genome(path: str):
    print("Genome utilise : " + path)
    (x, n), (y, m) = tools.get_genome(path)
    prog_dyn_test(x, y, n, m)


def test_dist_1():
    print("======== Test DIST_1 ========")
    print("TEST 1:")
    dist_1_test("A", "")
    print()

    print("TEST 2:")
    dist_1_test("A", "C")
    print()

    print("TEST 3:")
    dist_1_test("ATCG", "")
    print()

    print("TEST 4:")
    dist_1_test("", "ATCG")
    print()

    print("TEST 5:")
    dist_1_test("AT", "CG")
    print()

    print("TEST 6:")
    dist_1_test("ATTGTA", "ATCTTA")

    print("======== Fin Test DIST_1 ========")


def test_prog_dyn():
    print("======== Test PROG_DYN ========")
    print("TEST 1:")
    prog_dyn_test("ATTGTA", "ATCTTA")
    print()

    print("TEST 2:")
    prog_dyn_test("AT", "CG")

    print("======== Test PROG_DYN ========")


def test_genome_prog_dyn():
    print("======= Test Genome PROG_DYN =======")
    prog_dyn_test_genome("Instances_genome/Inst_0010000_7.adn")
    print("======= Fin Test Genome PROG_DYN =======")


def question_23():
    print("======== QUESTION 23 ========")
    print("PROG_DYN('BALLON', 'ROND') = ", tacheB.PROG_DYN("BALLON", "ROND"))
    print("PROG_DYN('BAL', 'RO') = ", tacheB.PROG_DYN("BAL", "RO"))
    print("PROG_DYN('LON', 'ND') = ", tacheB.PROG_DYN("LON", "ND"))


if __name__ == "__main__":
    test_dist_1()
    test_prog_dyn()
    # question_23()
    test_genome_prog_dyn()
