# ----------------------------------------------------------------------------------------------------------------------
# Funkcja do pobrania danych o artystach najczesciej sluchanych przez uzytkownika
# ----------------------------------------------------------------------------------------------------------------------

from db_handling import db_querry, db_truncate_table
from spotipy_connection import spotipy_connection

# Połączenie do API Spotify
sp = spotipy_connection()


# Zdefiniowanie funkcji wypełniającej bazę danymi uzyskanymi z odpytania API
def fill_top_artists_table(db_table_name, chosen_range):
    # Wyczyszczenie tabeli
    db_truncate_table(db_table_name)
    for sp_range in chosen_range:
        # Wyslanie zadania do API
        results = sp.current_user_top_artists(time_range=sp_range, limit=20)
        for i, item in enumerate(results['items']):
            position = i + 1
            id = item['id']
            uri = item['uri']
            name = item['name'].replace("'", "")
            genre = item['genres']
            genre1 = []
            image = item['images'][0]['url']
            # Wyciągnięcie tylko jednego gatunku w którym tworzy artysta
            if len(genre) >= 1:
                genre1.append(genre[0])
            else:
                genre1.append("")
                genre1[0].replace("'", "")
            # Wstawianie wyniku żądania API do tabeli bazy danych
            insert_record = f"insert into MusicWorld.dbo.{db_table_name} ([Position],[Artist_spotifyID],[Artist_uri],[Artist],[Genre],[Img_url])" \
                            f"VALUES('{position}','{id}','{uri}','{name}','{genre1[0]}','{image}')"
            db_querry(insert_record)
