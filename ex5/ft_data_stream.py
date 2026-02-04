from typing import Generator
import time


def finite_generator(max: int) -> Generator[int, None, None]:
    """Creates a generator instead of using range for the exercise"""
    i = 0
    if max < 0:
        return
    while i != max:
        yield i
        i += 1


def events_generator() -> Generator[str, None, None]:
    """Generates events"""
    while True:
        yield "killed a monster"
        yield "found treasure"
        yield "leveled up"
        yield "did nothing !"


def players_iterator() -> Generator[str, None, None]:
    """Iterates over players"""
    while True:
        yield "alice"
        yield "bob"
        yield "charlie"


def fibonacci_iter() -> Generator[int, None, None]:
    """Yields the Fibonacci sequence"""
    temp1 = 0
    yield 0
    temp2 = 1
    yield 1
    while True:
        res = temp1 + temp2
        temp1 = temp2
        temp2 = res
        yield res


def is_prime(nb: int) -> bool:
    """Returns True if the number is a prime"""
    if nb <= 1:
        return False
    i = 0
    for i in range(2, int(nb**(1 / 2)) + 1):
        if nb % i == 0:
            return False
    return True


def prime_iter() -> Generator[iter, None, None]:
    """Yield the next prime each time"""
    res = 2
    yield 2
    res += 1
    while True:
        if is_prime(res):
            yield res
        res += 1


def ft_test_generator() -> None:
    """Simulates events for 3 players"""
    players = {
        "alice": {"name": "alice", "level": 5, "treasures": 0},
        "bob": {"name": "bob", "level": 12, "treasures": 0},
        "charlie": {"name": "charlie", "level": 8, "treasures": 0}
    }
    level_events = 0
    treasure_events = 0
    high_level_count = 0
    for key in players.keys():
        if players[key]["level"] >= 10:
            high_level_count += 1
    nb_events = 1000
    player_name_iterator = players_iterator()
    event_iterator = events_generator()
    skip = False

    print("=== Game Data Stream Processor ===")
    print()
    print(f"Processing {nb_events} game events...")
    print()
    cur_time = time.time()
    for i in finite_generator(nb_events):
        cur_player = next(player_name_iterator)
        lvl = players[cur_player]["level"]
        event = next(event_iterator)
        if skip is False:
            print(f"Event {i + 1}: Player {cur_player} (level {lvl}) {event}")
        if skip is False and i >= 2:
            skip = True
            print("...")
        if event == "leveled up":
            players[cur_player]["level"] += 1
            if players[cur_player]["level"] == 10:
                high_level_count += 1
            level_events += 1
        if event == "found treasure":
            players[cur_player]["treasures"] += 1
            treasure_events += 1
    print()
    cur_time = time.time() - cur_time

    print("=== Stream Analytics ===")
    print()
    print(f"Total event processed: {nb_events}")
    print(f"High level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level_up_events: {level_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {cur_time:.4f} seconds")
    print()

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib_iter = fibonacci_iter()
    for i in range(9):
        print(f"{next(fib_iter)}, ", end="")
    print(f"{next(fib_iter)}")
    prime_iterator = prime_iter()
    print("Prime numbers (first 5): ", end="")
    for i in range(4):
        print(f"{next(prime_iterator)}, ", end="")
    print(f"{next(prime_iterator)}")


ft_test_generator()
