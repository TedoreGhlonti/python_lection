import requests

def get_artwork(query, limit):
    res = requests.get(
      "https://api.artic.edu/api/v1/artworks/search",
      {"q": query, "limit": limit} 
    )

    data = res.json()
    return [artwork["title"] for artwork in data["data"]]