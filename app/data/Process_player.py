from .NBA_api_fetch import fetch_player_stats
from ..models.player import Player
import pandas as pd

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

    # Convert PLAYER_NAME to string, then replace pd.NA with None
    df["PLAYER_NAME"] = df["PLAYER_NAME"].apply(
        lambda x: None if pd.isna(x) else x
    )

    for _, row in df.iterrows():
        fantasy_value = calculate_fantasy_value(row)

        player = Player(
            id=int(row['PLAYER_ID']),
            name=row['PLAYER_NAME'],       # now guaranteed str or None
            team=row['TEAM_ABBREVIATION'],
            games_played=int(row['GP']),
            ppg=float(row['PTS']),
            rpg=float(row['REB']),
            apg=float(row['AST']),
            fppg=float(fantasy_value),
            games_remaining=82 - int(row['GP']),
        )
        players.append(player)

    return players
