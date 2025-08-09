'''
This file fetches data from NBA api for the 2024-2025 season. However, once new season starts, it will fetch latest season instead.
This will help with more accurate predictions.
'''

from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

def fetch_player_stats(season='2024-25') -> pd.DataFrame:
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season, 
        season_type_all_star='Regular Season'
    )
    return stats.get_data_frames()[0]