from NBA_api_fetch import fetch_player_stats
from ..models.player import Player

def calculate_fantasy_value(row) -> float:
    val = (
        row["FGM"] * 2
        - row["FGA"]
        + row["FTM"]
        - row["FTA"]
        + row["FG3M"]
        + row["REB"]
        + row["AST"] * 2
        + row["STL"] * 4
        + row["BLK"] * 4
        - row["TOV"] * 2
        + row["PTS"]
        + row["DD2"] * 2
        + row["TD3"] * 5
    )
    return round(val, 2)


def get_all_players():
    df = fetch_player_stats()
    players = []

    for _, row in df.iterrows():
        fantasy_value = calculate_fantasy_value(row)

        player = Player(
            id=row['PLAYER_ID'],
            name=row['PLAYER_NAME'],
            team=row['TEAM_ABBREVIATION'],
            games_played=row['GP'],
            ppg=row['PTS'],
            rpg=row['REB'],
            apg=row['AST'],
            position=row['PlayerPosition'],
            fppg=fantasy_value,
            games_remaining=82-row['GP'],
            injury_status=None

        )

        players.append(player)

    return players
