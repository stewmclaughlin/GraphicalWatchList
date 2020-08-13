import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from GraphicalWatchList import HelperFunctions



def main_layout():
    return html.Div([
        html.Div([
            # Visualization Tabs
            dcc.Tabs(id="inline-tabs", value='main_layout', children=[
                dcc.Tab(label='Movies', value='movies', style=HelperFunctions.Style.tab_style(),
                        selected_style=HelperFunctions.Style.tab_selected_style()),
                dcc.Tab(
                    label='TV Shows',
                    value='tv',
                    style=HelperFunctions.Style.tab_style(),
                    selected_style=HelperFunctions.Style.tab_selected_style()),
                dcc.Tab(
                    label='Statistics',
                    value='stats',
                    style=HelperFunctions.Style.tab_style(),
                    selected_style=HelperFunctions.Style.tab_selected_style()),
                dcc.Tab(
                    label='Settings',
                    value='settings',
                    style=HelperFunctions.Style.tab_style(),
                    selected_style=HelperFunctions.Style.tab_selected_style()),
            ], style=HelperFunctions.Style.tabs_styles()),
            html.Div(id='tabs-content-inline')
        ])
    ])




def main():
    print("Hello World")



if __name__ == "__main__":
    main()