club = "Werder Bremen"
season = 3
competition = "Bundesliga"

wins = 3
draws = 2
losses = 6
goals_scored = 9
goals_conceded = 12

matches = wins + draws + losses
win_rate = wins / matches * 100
goal_difference = goals_scored - goals_conceded

print("===========================================================")
print("                 FIFA CAREER MODE")
print("===========================================================")
print("Club:", club)
print("Season:", season)
print("Competition:", competition)
print("Matches Played:", matches)
print("Record:", wins, "W", draws, "D", losses, "L", goal_difference, "GD")
print ("Win Rate:", round(win_rate, 1), "%")

print("===========================================================")
print("                 SEASON 3 MATCH DATA")
print("===========================================================")

matches_data = [
    {
        "opponent": "Schalke",
        "competition": "Bundesliga",
        "goals_for": 0,
        "goals_against": 1
    },
    {
        "opponent": "Bayer Leverkusen",
        "competition": "Bundesliga",
        "goals_for": 1,
        "goals_against": 2
    },
]

for match in matches_data:
    if match["goals_for"] > match["goals_against"]:
        result = "W"
    elif match["goals_for"] < match["goals_against"]:
        result = "L"
    else:
        result = "D"
    print(
        match["competition"],
        "|",
        match["opponent"],
        "|",
        match["goals_for"],
        "|",
        match["goals_against"],
        "|",
        result
)

print("===========================================================")
print("                 COMPETITION TOTALS")
print("===========================================================")
competitions = [
    "Bundesliga",
    "DFB-Pokal",
    "UEFA Champions League",
    "UEFA Europa League",
    "UEFA Conference League"
]
for competition_name in competitions:
    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0

    for match in matches_data:
        if match["competition"] == competition_name:
            goals_for += match["goals_for"]
            goals_against += match ["goals_against"]
            if match["goals_for"] > match["goals_against"]:
                wins += 1
            elif match["goals_for"] < match["goals_against"]:
                losses += 1
            else:
                draws += 1

    matches = wins + draws + losses
    goal_difference = goals_for - goals_against

    print()
    print("===========================================================")
    print(competition_name.upper())
    print("===========================================================")
    print("Matches:", matches)
    print("Wins:", wins)
    print("Draws:", draws)
    print("Losses:", losses)
    print("GF:", goals_for)
    print("GA:", goals_against)
    print("GD:", goal_difference)