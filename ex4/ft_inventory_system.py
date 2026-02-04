import sys


def parsing_input(argv: list[str]) -> dict[str:dict[str, int]] | None:
    """Parses the input or raises an error if the format is incorrect"""
    res = {}
    try:
        for entry in argv:
            temp = entry.split(sep=":")
            if len(temp) != 2:
                raise Exception(
                    "Invalid input, use <item1>:<qty1> <item2>:<qty2>...")
            res.update({temp[0]: {"name": temp[0], "qty": int(temp[1])}})
    except Exception:
        raise Exception("Invalid input, use <item1>:<qty1> <item2>:<qty2>...")
    return res


def ft_test_dict(argv: list[str]) -> None:
    """Uses dictionnary to simulate arguments"""
    try:
        inv = parsing_input(argv)
    except Exception as cur_error:
        print(cur_error)
        return
    if len(argv) == 0:
        print("Please input an inventory: <item1>:<qty1> <item2>:<qty2>...")
        return

    print("=== Inventory System Analysis ===")
    total = 0
    for item in inv.values():
        total += item['qty']
    qty = 0
    for item in inv.values():
        qty += 1
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {qty}")
    print()

    print("=== Current Inventory ===")
    for key, item in inv.items():
        value = (item['qty'] / total * 100)
        print(f"{key}: {item['qty']} units ({value:.2f}%)")
    print()

    print("=== Inventory Statistics ===")
    min_item = None
    max_item = None
    for item in inv.values():
        qty = item.get("qty")
        if min_item is None or qty < min_item.get("qty"):
            min_item = item
        if max_item is None or qty > max_item.get("qty"):
            max_item = item
    if max_item["qty"] <= 1:
        print(f"Most abundant: {max_item['name']} ({max_item['qty']} unit)")
    else:
        print(f"Most abundant: {max_item['name']} ({max_item['qty']} units)")
    if min_item['qty']:
        print(f"Least abundant: {min_item['name']} ({min_item['qty']} unit)")
    else:
        print(f"Least abundant: {min_item['name']} ({min_item['qty']} units)")
    print()

    print("=== Item Categories ===")
    moderate = {value['name']: value['qty']
                for value in inv.values() if value['qty'] >= 5}
    scarce = {
        value['name']: value['qty']
        for value in inv.values() if value['qty'] < 5}
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")
    print()

    print("=== Management Suggestion ===")
    restock = [value["name"] for value in inv.values() if value['qty'] <= 1]
    if restock:
        print(f"Restock needed: {restock}")
    else:
        print("No restock needed")
    print()

    print("=== Dictionary properties Demo ===")
    print(f"Dictionary keys: {inv.keys()}")
    print(
        f"Dictionnary values: {[item['qty'] for item in inv.values()]}")
    print(
        f"Sample lookup - 'sword' in inventory: {'sword' in inv.keys()}")


if __name__ == "__main__":
    test = sys.argv[1:]
    ft_test_dict(test)
