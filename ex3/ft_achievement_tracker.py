def test_sets() -> None:
    """Uses sets to get achievements"""
    print("=== Achievment Tracker system ===")
    print()
    # Creation of unique achievements
    first_kill = "first_kill"
    lvl_ten = "level_10"
    treasure_hunter = "treasure_hunter"
    speed_demon = "speed_demon"
    boss_slayer = "boss_slayer"
    collector = "collector"
    perfectionnist = "perfectionist"
    # Creation of achievements sets
    alice = {first_kill, lvl_ten, treasure_hunter, speed_demon}
    bob = {first_kill, lvl_ten, boss_slayer, collector}
    charlie = {lvl_ten,
               treasure_hunter,
               boss_slayer,
               speed_demon,
               perfectionnist}
    print(f"Player alice achievements: {alice})")
    print(f"Player bob achievements: {bob})")
    print(f"Player charlie achievements: {charlie})")
    print()
    print("=== Achievement Analytics ===")
    total = alice | bob | charlie
    common = alice & bob & charlie
    unique = (alice ^ bob ^ charlie) - common
    print(f"All unique achievements: {total}")
    print(f"Total unique achievements: {len(total)}")
    print()
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {unique}")
    print()
    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    test_sets()
