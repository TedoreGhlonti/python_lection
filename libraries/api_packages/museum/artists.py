import requests

def get_artists(query, limit):
    res = requests.get(
        "https://api.artic.edu/api/v1/agents/search",
        {"q": query, "limit": limit}
    )

    data = res.json()
    return [artists["title"] for artists in data["data"]]