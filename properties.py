c_del = 2
c_ins = 2
alphabet = {"A", "T", "G", "C"}


def c_sub(a: str, b: str) -> int:
    if a == b:
        return 0
    if {a, b} == {"A", "B"} or {a, b} == {"C", "G"}:
        return 3
    else:
        return 4