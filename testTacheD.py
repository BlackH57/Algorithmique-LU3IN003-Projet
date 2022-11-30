import tools
import tacheD

if __name__ == "__main__":
    print(tacheD.align_lettre_mot("A", "AAAA"))
    print(tacheD.align_lettre_mot("A", "CCCC"))
    print(tacheD.align_lettre_mot("A", "ATCG"))
    print(tacheD.align_lettre_mot("A", "TCAG"))

    print(tacheD.SOL_2("AT", "CG"))
    print(tacheD.SOL_2("ATTGTA", "ATCTTA"))

    print(tacheD.SOL_2("AGTACGCA", "TATGC"))
