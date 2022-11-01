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
