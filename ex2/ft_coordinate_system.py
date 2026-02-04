from math import sqrt


def str_to_tuple(arg: str) -> tuple:
    """Parse the position passed as an argument"""
    try:
        res = arg.split(sep=",")
        res = tuple(res)
    except AttributeError:
        raise AttributeError(f"Invalid input: {arg}")
    return res


def check_is_coordinates(arg: tuple) -> tuple | None:
    """Checks if the tuple passed as an argument is a valid coordinate.
    Now using int() without try/except because it raises its own ValueError"""
    if len(arg) != 3:
        raise ValueError("Tuple has more than 3 elements")
    for i in arg:
        int(i)
    return ((int(arg[0]), int(arg[1]), int(arg[2])))


def parse_coordinates(arg: str) -> tuple | None:
    """Parses a tuple"""
    try:
        res = str_to_tuple(arg)
        res = check_is_coordinates(res)
        return (res)
    except (ValueError, AttributeError) as cur_error:
        res = f"Error parsing coordinates: {cur_error}\n"
        res = res + f"Error details - Type: {cur_error.__class__.__name__},"
        res = res + f" Args: (\"{cur_error}\")"
        raise ValueError(res)


def ft_distance(arg1: tuple, arg2: tuple) -> float | None:
    """Returns the distance between 2 points"""
    try:
        check_is_coordinates(arg1)
        check_is_coordinates(arg2)
    except ValueError as cur_error:
        raise ValueError(cur_error)
    x_val = (arg1[0] - arg2[0])**2
    y_val = (arg1[1] - arg2[1])**2
    z_val = (arg1[2] - arg2[2])**2
    dist = sqrt(x_val + y_val + z_val)
    print(f"Distance between {arg1} and {arg2}: {dist:.2f}")
    return (dist)


def test_coordinates() -> None:
    """Tests the coordinates system"""
    print("=== Game Coordinate System ===")
    print()
# Testing a valid position:
    try:
        pos1 = parse_coordinates("10,20,5")
        print(f"Position created: {pos1}")
        ft_distance(pos1, (0, 0, 0))
    except Exception as cur_error:
        print(cur_error)
    print()
    pos2 = "3,4,0"
    print(f"Parsing coordinates: {pos2}")
    try:
        pos2 = parse_coordinates(pos2)
        print(f"Parsed position: {pos2}")
        ft_distance(pos2, (0, 0, 0))
    except ValueError as cur_error:
        print(cur_error)
    print()
# Testing an invalid position
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    try:
        parse_coordinates("abc,def,ghi")
    except ValueError as cur_error:
        print(cur_error)
    print()
# Unpacking demonstration
    print("Unpacking demonstration:")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    test_coordinates()
