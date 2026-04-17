import sys
import requests

def main():
    try:
        res = requests.get("https://api.artic.edu/api/v1/artworks/search")
    except requests.HTTPError:
        print("Could not complete request")
        sys.exit(1)
    content = res.json()
    for artwork in content["data"]:
        print(f"[*] {artwork['title']}")

main()

