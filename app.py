# ----------------------------------------------------------------------------------------------------------------------
# Tworzenie aplikacji przegladarkowej
# ----------------------------------------------------------------------------------------------------------------------
# przygotowano na podstawie: https://www.youtube.com/watch?v=RMBSQ6leonU

import dash

# Definiowanie obiektu aplikacji
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

# Definiowanie serwera
server = app.server
