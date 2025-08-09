### Web scraper for injuries
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def scrape_injuries():
    url = "https://www.basketball-reference.com/friv/injuries.fcgi"
    response = requests.get(url)
    # print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    injury_table = soup.find('table', id='injuries')
    # if not injury_table:
    #     print("❌ Table not found!")
    # else:
    #     print("✅ Table found!")

    # Loop through rows
    injuries = {}

    for row in injury_table.tbody.find_all("tr"):
        player_cell = row.find("th", {"data-stat": "player"})
        team_cell = row.find("td", {"data-stat": "team_name"})
        update_cell = row.find("td", {"data-stat": "date_update"})
        note_cell = row.find("td", {"data-stat": "note"})

        player_name = player_cell.get_text(strip=True)
        team = team_cell.get_text(strip=True)
        update = update_cell.get_text(strip=True)
        note = note_cell.get_text(strip=True)

        # print(f"Player: {player_name} | Team: {team} | Updated: {update} | Note: {note}")

        injuries[player_name]=[player_name,team,update,note]

    return injuries
