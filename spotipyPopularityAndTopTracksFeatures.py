# ----------------------------------------------------------------------------------------------------------------------
# Funkcje do pobrania danych o popularnosci oraz cech utworow
# ----------------------------------------------------------------------------------------------------------------------

import pandas as pd
from db_handling import db_read_column_to_table
from spotipy_connection import spotipy_connection

# Połączenie do API Spotify
sp = spotipy_connection()

list_track_uri = db_read_column_to_table('track_uri', 'Top_tracks_longterm')
list_artist_uri = db_read_column_to_table('artist_uri', 'Top_artists_longterm')


# Pobranie cech utworow i ich popularnosci
# przygotowano na podstawie: https://medium.com/@m.w.bochniewicz/music-analysis-with-python-part-1-create-your-own-dataset-with-lastfm-and-spotify-8223a46fad4b

def get_audio_features(list_track_uri):
    artist = []
    track = []
    popularity = []
    danceability = []
    energy = []
    valence = []
    for uri in list_track_uri:
        table_track_features = sp.audio_features(uri)
        table_track_name = sp.track(uri)

        for audio_features in table_track_features:
            danceability.append(audio_features['danceability'])
            energy.append(audio_features['energy'])
            valence.append(audio_features['valence'])

        artist.append(table_track_name['album']['artists'][0]['name'])
        track.append(table_track_name['name'])
        popularity.append(table_track_name['popularity'])

    df = pd.DataFrame()
    df['artist'] = artist
    df['track'] = track
    df['popularity'] = popularity
    df['danceability'] = danceability
    df['energy'] = energy
    df['valence'] = valence
    return df

# Pobranie popularnosci artystow
def get_artists_popularity(list_artist_uri):
    artist = []
    popularity = []
    for uri in list_artist_uri:
        table_artist_name = sp.artist(uri)
        artist.append(table_artist_name['name'])
        popularity.append(table_artist_name['popularity'])
    df = pd.DataFrame()
    df['artist'] = artist
    df['popularity'] = popularity
    return df
