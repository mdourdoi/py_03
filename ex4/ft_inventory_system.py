def ft_test_dict() -> None:
    """Uses dictionnary to simulate arguments"""
    print("=== Inventory system analysis ===")
    inventory = {
        "potion": {
            "name": "potion",
            "quantity": 5},
        "armor": {
            "name": "armor",
            "quantity": 3},
        "shield": {
            "name": "shield",
            "quantity": 2},
        "sword": {
            "name": "sword",
            "quantity": 1},
        "helmet": {
            "name": "helmet",
            "quantity": 1}}
    total = 0
    for item in inventory.values():
        total += item["quantity"]
    quantity = 0
    for item in inventory.values():
        quantity += 1
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {quantity}")
    print()
    print("=== Current Inventory ===")
    for key, item in inventory.items():
        value = (item["quantity"] / total * 100)
        print(f"{key}: {item["quantity"]} units ({value:.2f}%)")
    print()
    print("=== Item Categories ===")
    moderate = {
        value["name"]: value["quantity"]
        for value in inventory.values() if value["quantity"] >= 5}
    scarce = {
        value["name"]: value["quantity"]
        for value in inventory.values() if value["quantity"] < 5}
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")
    print()
    print("=== Management Suggestion ===")
    restock = [value["name"]
               for value in inventory.values() if value["quantity"] <= 1]
    if restock:
        print(f"Restock needed: {restock}")
    else:
        print("No restock needed")
    print()
    print("=== Dictionary properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(
        f"Dictionnary values: {[item["quantity"] for item in inventory.values()]}")
    print(
        f"Sample lookup - 'sword' in inventory: {"sword" in inventory.keys()}")


ft_test_dict()
