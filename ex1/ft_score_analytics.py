import sys


def check_validity(argv: list[str]) -> list[int] | None:
    """Transforms the string list into a int list"""
    res = []
    for score in argv:
        try:
            res.append(int(score))
        except ValueError:
            raise ValueError(f"'{score}' is not a valid number")
    return res


def score_analytics(args: list[int]) -> None:
    """Displays informations about the scores"""
    if len(args) > 0:
        print(f"Scores processed: {args}")
        print(f"Total players: {len(args)}")
        print(f"Total score: {sum(args)}")
        print(f"Average core: {sum(args) / len(args)}")
        print(f"High score: {max(args)}")
        print(f"Low score: {min(args)}")
        print(f"Score range: {max(args) - min(args)}")
    else:
        print("No score provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2>")


def main(argv: list[str]) -> None:
    """Orchestrates the validation + display of the scores"""
    print("=== Player Score Analytics ===")
    try:
        score_analytics(check_validity(argv))
    except ValueError as cur_error:
        print(f"Error: {cur_error}")


if __name__ == "__main__":
    main(sys.argv[1:])
