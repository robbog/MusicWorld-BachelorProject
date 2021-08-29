# ----------------------------------------------------------------------------------------------------------------------
# Szkielet witryny
# ----------------------------------------------------------------------------------------------------------------------
# Aby uruchomic cala aplikacje przegladarkowa nalezy uruchomic ten modul
# przygotowano na podstawie: https://www.youtube.com/watch?v=RMBSQ6leonU

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# Polaczenie z plikiem app.py tworzacym aplikacje
from app import app

# Polaczenie z podstronami
from apps import about, dashboard


# Przygotowanie layoutu witryny
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])

# Backend witryny
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/dashboard':
        return dashboard.layout
    else:
        return about.layout

# Pętla witryny
if __name__ == '__main__':
    app.run_server(debug=False)
