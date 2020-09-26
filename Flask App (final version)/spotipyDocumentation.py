import spotipy_connection

sp = spotipy_connection.spotipy_connection()
results = sp.current_user_playlists(limit=20)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))
"""

artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,10000,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])


import pandas as pd
track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})
print(track_dataframe.shape)
track_dataframe.head()
"""

"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="01115ffe9468483c87e7bc0d102c4eb0",
                                                           client_secret="18d5679ff15c44ca801fedadeb8000ed"))

results = sp.search(q='pink_floyd', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
"""
