import json
import os

FAVORITES_FILE = "favorites.json"

def load_favorites():
    if not os.path.exists(FAVORITES_FILE):
        return []
    with open(FAVORITES_FILE, "r") as f:
        return json.load(f)

def save_favorites(favorites):
    with open(FAVORITES_FILE, "w") as f:
        json.dump(favorites, f, indent=2)

def add_favorite(city):
    favorites = load_favorites()
    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)
        return True
    return False

def remove_favorite(city):
    favorites = load_favorites()
    if city in favorites:
        favorites.remove(city)
        save_favorites(favorites)
        return True
    return False