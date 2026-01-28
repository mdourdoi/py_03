import sys


def main(argv: list[str]) -> None:
    """Displays the arguments given"""
    if len(argv) == 1:
        print("No arguments provided")
    else:
        argv_len = len(argv[1:])
        for i in range(argv_len):
            print(f"Argument {i + 1}: {argv[i + 1]}")
    print(f"Program name: {argv[0]}")
    print(f"Total arguments: {len(argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main(sys.argv)
