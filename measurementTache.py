import tools
import tacheA
import tacheB
import tacheC
import tacheD


# Commencons par analyser la tache A


def measurementTacheA():
    ntm = tools.memory_time_consumption(tacheA.DIST_NAIF, allowed_time=1)
    tools.write_info_list(ntm, tacheA.DIST_NAIF)
    # tools.plot_information_from_list(ntm, mode=0, name="DIST_NAIF")
    # tools.plot_information_from_list(ntm, mode=1)


def measurementTacheB():
    ntm = tools.memory_time_consumption(tacheB.PROG_DYN, allowed_time=10)
    tools.write_info_list(ntm, tacheB.PROG_DYN)
    # tools.plot_information_from_list(ntm, mode=0, name="PROG_DYN")
    # tools.plot_information_from_list(ntm, mode=1, name="PROG_DYN")


def measurementTacheC():
    ntm = tools.memory_time_consumption(tacheC.DIST_2, allowed_time=10)
    tools.write_info_list(ntm, tacheC.DIST_2)
    # tools.plot_information_from_list(ntm, mode=0, name="DIST_2")
    # tools.plot_information_from_list(ntm, mode=1, name="DIST_2")


def measurementTacheD():
    ntm = tools.memory_time_consumption(tacheD.SOL_2, allowed_time=10)
    tools.write_info_list(ntm, tacheD.SOL_2)
    # tools.plot_information_from_list(ntm, mode=0, name="SOL_2")
    # tools.plot_information_from_list(ntm, mode=1, name="SOL_2")


if __name__ == "__main__":
    measurementTacheA()
    measurementTacheB()
    measurementTacheC()
    measurementTacheD()

    # lntm = tools.read_info_list("memory_and_time/DIST_NAIF.txt")
    # tools.plot_information_from_list(lntm, 0, "DIST_NAIF")
    # tools.plot_information_from_list(lntm, 1, "DIST_NAIF")

    # lntm = tools.read_info_list("memory_and_time/PROG_DYN.txt")
    # tools.plot_information_from_list(lntm, 0, "PROG_DYN")
    # tools.plot_information_from_list(lntm, 1, "PROG_DYN")

    # lntm = tools.read_info_list("memory_and_time/DIST_2.txt")
    # tools.plot_information_from_list(lntm, 0, "DIST_2")
    # tools.plot_information_from_list(lntm, 1, "DIST_2")

    # lntm = tools.read_info_list("memory_and_time/SOL_2.txt")
    # tools.plot_information_from_list(lntm, 0, "SOL_2")
    # tools.plot_information_from_list(lntm, 1, "SOL_2")
