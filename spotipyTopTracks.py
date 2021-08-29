# ----------------------------------------------------------------------------------------------------------------------
# Funkcja do pobrania danych o utworach najczesciej sluchanych przez uzytkownika
# ----------------------------------------------------------------------------------------------------------------------

from db_handling import db_querry, db_truncate_table, db_read_columns_to_pandas
from spotipy_connection import spotipy_connection

# Połączenie do API Spotify
sp = spotipy_connection()


# Zdefiniowanie funkcji wypełniającej bazę danymi uzyskanymi z odpytania API
def fill_top_tracks_table(db_table_name, chosen_range):
    # Wyczyszczenie tabeli
    db_truncate_table(db_table_name)
    for sp_range in chosen_range:
        # Wyslanie zadania do API
        results: object = sp.current_user_top_tracks(time_range=sp_range, limit=20)
        for i, item in enumerate(results['items']):
            Position = i + 1
            id = item['id']
            uri = item['uri']
            name = item['name'].replace("'", "")
            artist = item['artists'][0]['name'].replace("'", "")
            album = item['album']['name'].replace("'", "")
            image = item['album']['images'][0]['url']
            popularity = sp.track(uri)['popularity']
            table_track_features = sp.audio_features(uri)
            danceability = table_track_features[0]['danceability']
            energy = table_track_features[0]['energy']
            valence = table_track_features[0]['valence']
            # Wstawianie wyniku żądania API do tabeli bazy danych
            insert_record = f"insert into Musicworld.dbo.{db_table_name} ([Position],[Track_spotifyID],[Track_uri],[Title],[Artist],[Album],[Img_url], [Track_popularity],[Track_danceability],[Track_energy],[Track_valence]) " \
                            f"VALUES('{Position}','{id}','{uri}','{name}','{artist}','{album}','{image}','{popularity}','{danceability}','{energy}','{valence}')"
            db_querry(insert_record)
