import math


def str_to_tuple(arg: str) -> tuple:
    """Parse the position passed as an argument"""
    return tuple(arg.split(sep=","))


if __name__ == "__main__":
    print(str_to_tuple("12,45,23"))
