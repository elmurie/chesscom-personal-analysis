import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

username = input("insert chess.com username: ").strip().lower()

headers = {
    "User-Agent": "chess-data-analysis-script/1.0"
}

# src/ -> chess-analytics/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# dataset/raw/{username}/
dataset_dir = PROJECT_ROOT / "dataset" / "raw" / username
dataset_dir.mkdir(parents=True, exist_ok=True)

base_url = f"https://api.chess.com/pub/player/{username}"


def get_json(url):
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Request failed: {url}")
        print("Status:", response.status_code)
        print(response.text[:500])
        return None

    try:
        return response.json()
    except Exception:
        print(f"Invalid JSON from: {url}")
        print(response.text[:500])
        return None


# 1. Player profile
profile = get_json(base_url)

if profile:
    profile_df = pd.json_normalize(profile)

    profile_path = dataset_dir / "profile.csv"

    profile_df.to_csv(profile_path, index=False)

    print(f"Profile saved in: {profile_path}")


# 2. General stats
stats = get_json(f"{base_url}/stats")

if stats:
    stats_df = pd.json_normalize(stats)

    stats_path = dataset_dir / "stats.csv"

    stats_df.to_csv(stats_path, index=False)

    print(f"Stats saved in: {stats_path}")


# 3. Games archives
archives_data = get_json(f"{base_url}/games/archives")

if not archives_data:
    raise SystemExit("Could not download archives")

archives = archives_data.get("archives", [])

all_games = []

for archive in archives:

    data = get_json(archive)

    if not data:
        continue

    for game in data.get("games", []):

        all_games.append({

            "date": (
                datetime.fromtimestamp(
                    game.get("end_time")
                ).strftime("%Y-%m-%d %H:%M:%S")
                if game.get("end_time")
                else None
            ),

            "url": game.get("url"),
            "uuid": game.get("uuid"),

            "time_class": game.get("time_class"),
            "time_control": game.get("time_control"),

            "rated": game.get("rated"),
            "rules": game.get("rules"),

            "white": game.get("white", {}).get("username"),
            "black": game.get("black", {}).get("username"),

            "white_rating": game.get("white", {}).get("rating"),
            "black_rating": game.get("black", {}).get("rating"),

            "result_white": game.get("white", {}).get("result"),
            "result_black": game.get("black", {}).get("result"),

            "eco": game.get("eco"),

            "pgn": game.get("pgn")
        })

games_df = pd.DataFrame(all_games)

games_path = dataset_dir / "games.csv"

games_df.to_csv(games_path, index=False)

print(f"Games saved in: {games_path}")
print(f"Saved {len(games_df)} games")
print(games_df.head())