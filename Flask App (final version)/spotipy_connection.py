def spotipy_connection():
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="01115ffe9468483c87e7bc0d102c4eb0",
                                                   client_secret="18d5679ff15c44ca801fedadeb8000ed",
                                                   redirect_uri="http://localhost:8888",
                                                   scope="user-library-read"))
    return sp