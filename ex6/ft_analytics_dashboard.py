def ft_analytics_tests() -> None:
    print("=== Game Analytics Dashboard ===")
    print()
    first_kill = "first_kill"
    lvl_ten = "level_10"
    treasure_hunter = "treasure_hunter"
    speed_demon = "speed_demon"
    boss_slayer = "boss_slayer"
    collector = "collector"
    perfectionnist = "perfectionist"
    # Creation of achievements sets
    alice_ach = {first_kill, lvl_ten, treasure_hunter, speed_demon}
    bob_ach = {first_kill, lvl_ten, boss_slayer, collector}
    charlie_ach = {
        lvl_ten,
        treasure_hunter,
        boss_slayer,
        speed_demon,
        perfectionnist}
    players = {
        "alice": {
            "name": "alice",
            "score": 2300,
            "is_active": True,
            "achievements": alice_ach,
            "region": "north"},
        "bob": {
            "name": "bob",
            "score": 1800,
            "is_active": True,
            "achievements": bob_ach,
            "region": "east"},
        "charlie": {
            "name": "charlie",
            "score": 2150,
            "is_active": True,
            "achievements": charlie_ach,
            "region": "central"},
        "diana": {
            "name": "diana",
            "score": 2050,
            "is_active": False,
            "achievements": {},
            "region": "south"}}

    print("=== List Comprehension Examples ===")
    high_scores = [players[key]["name"]
                   for key in players.keys() if players[key]["score"] > 2000]
    score_doubled = [players[key]["score"] * 2 for key in players.keys()]
    actives = [players[key]["name"]
               for key in players.keys() if players[key]["is_active"]]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {actives}")
    print()

    print("=== Dict Comprehension Examples ===")
    scores = {players[key]["name"]: players[key]["score"]
              for key in players.keys() if players[key]["is_active"]}
    high = {players[key]["name"]
            for key in players.keys() if players[key]["score"] > 2200}
    medium = {players[key]["name"]
              for key in players.keys()
              if 2200 >= players[key]["score"] > 2000}
    low = {players[key]["name"]
           for key in players.keys() if players[key]["score"] <= 2000}
    score_categories = {
        "high": len(high),
        "medium": len(medium),
        "low": len(low)}
    ach_count = {players[key]["name"]: len(players[key]["achievements"])
                 for key in players.keys()}
    print(f"Player scores: {scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {ach_count}")
    print()

    print("=== Set comprehension Example ===")
    unique_players = {players[key]['name'] for key in players.keys()}
    unique_ach = {ach for player in players.values()
                  for ach in player["achievements"]}
    active_regions = {players[key]["region"]
                      for key in players.keys() if players[key]["is_active"]}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {active_regions}")
    print()

    print("=== Combined Analysis ===")
    scores = [players[key]["score"] for key in players.keys()]
    print(f"Total players: {len(players)}")
    print(f"Total unique achievments: {len(unique_ach)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    top = max((players[name]["score"],
               len(players[name]["achievements"]),
               name) for name in players.keys())
    res = f"Top performer: {top[2]} ({top[0]} points, {top[1]} achievements)"
    print(res)


if __name__ == "__main__":
    ft_analytics_tests()
