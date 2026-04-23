from museum.artists import get_artists
from  museum.artworks import get_artwork
def main():
    user = input('Artist: ').capitalize()
    #artists = get_artists(query=user, limit=3)
    artworks = get_artwork(query=user, limit=3)
    for artwork in artworks:
        print(f"[*] {artwork}")

    


main()