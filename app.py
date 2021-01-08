import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

## SOME DATASET PREPARATION
df = pd.read_csv('Airport_Traffic_Data.csv')
df = df.dropna()
df = df.astype({"DATA": int})
df['Foreign Airport'] = df['Foreign Airport'].str.split(')').str[0] + ')'

## START THE APP LAYOUT

app = dash.Dash(__name__, meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1"}
            ])
app.layout = html.Div([

    ## The div contains the app title and two top clip art pics
    html.Div([  # Title banner
        html.Div([
            html.Img(
                src='assets/plane-clipart-transparent-15.png',
                alt='Plane clip art',
                height='120px',
                style={'float': 'right'}
            ),
        ],
        ),
        html.Div([
            html.H3("Passenger Movement Through Irish Airports", style={'text-align': 'center'})
        ],
        ),
        html.Div([
            html.Img(
                src='assets/flag_irish.png',
                alt='Ireland clip art',
                height='120px',
            ),
        ],
        ),
    ],
        className='app-header',
    ),

    ## The div contains the middle section of the options box and map box
    html.Div([  # Div for selection components
        html.Div([
            html.Div([  # Div for selection components
                html.H6('Choose an Irish airport'),
                dcc.Dropdown(
                    id='selected_irish_airport',
                    options=[
                        {'label': 'Donegal (CFN)', 'value': 'CFN Donegal (CFN),Republic Of Ireland'},
                        {'label': 'Dublin (DUB)', 'value': 'DUB Dublin (DUB),Republic Of Ireland'},
                        {'label': 'Kerry (KIR)', 'value': 'KIR Kerry County (KIR),Republic Of Ireland'},
                        {'label': 'Knock (NOC)',
                         'value': 'NOC Knock - Ireland West (NOC),Republic Of Ireland'},
                        {'label': 'Cork (ORK)', 'value': 'ORK Cork (ORK),Republic Of Ireland'},
                        {'label': 'Shannon (SNN)', 'value': 'SNN Shannon (SNN),Republic Of Ireland'},
                    ],
                    value='DUB Dublin (DUB),Republic Of Ireland',
                    style={'color': 'black'}
                ),
            ],
                className='row selections'
            ),
            html.Div([
                html.H6('Choose a time period'),
                dcc.RangeSlider(
                    id='date_range',
                    min=2006,
                    max=2020,
                    step=1,
                    value=[2015, 2020],
                    marks={
                        2006: {'label': '2006'},
                        2008: {'label': '2008'},
                        2010: {'label': '2010'},
                        2012: {'label': '2012'},
                        2014: {'label': '2014'},
                        2016: {'label': '2016'},
                        2018: {'label': '2018'},
                        2020: {'label': '2020'}
                    },
                ),
            ],
                className='row selections',
            ),
            html.Div([
                html.Div([
                    html.H6('Choose a direction'),
                    dcc.RadioItems(
                        id='direction',
                        options=[
                            {'label': 'Outward', 'value': 'Outward'},
                            {'label': 'Inward', 'value': 'Inward'},
                        ],
                        value='Outward',
                        labelStyle={'display': 'inline-block'}
                    ),
                ],
                    className='selections'
                ),
                html.Div([
                    html.H6('Choose a chart scale'),
                    dcc.RadioItems(
                        id='lin-log-option',
                        options=[
                            {'label': 'linear', 'value': 0},
                            {'label': 'log', 'value': 1},
                        ],
                        value=0,
                        labelStyle={'display': 'inline-block'}
                    ),
                ],
                    className='selections'
                ),
            ],
                className='direction-scale-grid'
            ),
        ],
        ),
        html.Div([
            html.Div([
                html.H6('Choose a map style'),
                html.Div([
                    html.Div([
                        html.Img(
                            src='assets/lay1.png',
                            alt='im1',
                            height='100%',
                            width='100%'
                        )
                    ]),
                    html.Div([
                        html.Img(
                            src='assets/lay2.png',
                            alt='im2',
                            height='100%',
                            width='100%'
                        )

                    ]),  # map layout images
                    html.Div([
                        html.Img(
                            src='assets/lay3.png',
                            alt='im3',
                            height='100%',
                            width='100%'
                        )
                    ])  # map layout radio items
                ],
                    className='map-layouts'
                ),

                html.Div([
                    dcc.RadioItems(
                        id='map-style',
                        options=[
                            {'label': 'Street Map', 'value': 1},
                            {'label': 'Darkmatter', 'value': 2},
                            {'label': 'Satellite', 'value': 3},
                        ],
                        value=1,
                        labelStyle={'display': 'inline-block'},
                        className='radio-item'
                    ),

                ],
                ),
            ],
                className='row selections'
            ),
            html.Div([
                html.H6('Filter by Country'),
                dcc.Dropdown(
                    id='country_dropdown',
                    multi=True,
                    value=[],
                )
            ],
                className='row selections'
            ),
        ],
        )
    ],
        className='settings-box'
    ),

    html.Div([
        html.Div([
            html.P('Time Period'),
            html.P(id='time-info-text', style={'font-weight': 'normal'}),
        ], className='mini-info-box'),

        html.Div([
            html.P('Total trips'),
            html.P(id='trips-info-text', style={'font-weight': 'normal'}),
        ], className='mini-info-box'),

        html.Div([
            html.P('Top Location'),
            html.P(id='location-info-text', style={'font-weight': 'normal'}),
        ], className='mini-info-box')

    ],
        className='info-box'
    ),

    ## This div contains the two graphs at the bottom
    html.Div([
        html.Div([
            html.H5(id='bar_title_text',
                    style={'text-align': 'center'}
                    ),
            dcc.Graph(
                id='top_10_bar',
                figure={},
                config={
                    'displayModeBar': False
                },
            )
        ],
            className='graph-box'
        ),

        html.Div([
            html.H5(id='map_title_text',
                    style={'text-align': 'center'}
                    ),
            dcc.Graph(
                id='map',
                figure={},
            ),

        ],
            className='graph-box'
        )
    ],
        className='graphs-container',
    )
],
)

## A few reference dicts to control map layout ect..
map_layouts = {
    1: {'layout': 'open-street-map', 'color': 'inferno', 'size': 'DATA'},
    2: {'layout': 'carto-darkmatter', 'color': 'pinkyl', 'size': None},
    3: {'layout': 'white-bg', 'color': 'magenta', 'size': None}
}
irish_airports_dict = {
    'CFN Donegal (CFN),Republic Of Ireland': 'Donegal',
    'DUB Dublin (DUB),Republic Of Ireland': 'Dublin',
    'KIR Kerry County (KIR),Republic Of Ireland': 'Kerry',
    'NOC Knock - Ireland West (NOC),Republic Of Ireland': 'Knock',
    'ORK Cork (ORK),Republic Of Ireland': 'Cork',
    'SNN Shannon (SNN),Republic Of Ireland': 'Shannon'
}

bar_scales = {
    0: False,
    1: True
}
@app.callback(
    [Output(component_id='country_dropdown', component_property='options')],
    [Input(component_id='selected_irish_airport', component_property='value'),
     Input(component_id='direction', component_property='value'),
     Input(component_id='date_range', component_property='value')]
)
def update_country_options(irish_airport, direction, rangeBar):
    sub_df = df.copy()
    sub_df = sub_df[sub_df['Direction'] == direction]
    sub_df = sub_df[
        (sub_df.Month.str[0:4] >= str(rangeBar[0])) & (sub_df.Month.str[0:4] <= str(int(str(rangeBar[1]))))]
    sub_df = sub_df[sub_df['Irish Airport'] == irish_airport]
    sub_df = sub_df[sub_df['DATA'] != 0]
    countries = sorted(sub_df['Country'].unique())
    county_options = [
        {"label": str(county), "value": str(county)} for county in countries
    ]
    return [county_options]


@app.callback(
    [Output(component_id='map', component_property='figure'),
     Output(component_id='top_10_bar', component_property='figure'),
     Output(component_id='bar_title_text', component_property='children'),
     Output(component_id='map_title_text', component_property='children'),
     Output(component_id='time-info-text', component_property='children'),
     Output(component_id='trips-info-text', component_property='children'),
     Output(component_id='location-info-text', component_property='children'),
     ],
    [Input(component_id='selected_irish_airport', component_property='value'),
     Input(component_id='direction', component_property='value'),
     Input(component_id='date_range', component_property='value'),
     Input(component_id='map-style', component_property='value'),
     Input(component_id='country_dropdown', component_property='value'),
     Input(component_id='lin-log-option', component_property='value')
     ]
)
def update_graph(irish_airport, direction, rangeBar, mapStyle, country_list, bar_scale):
    sub_df = df.copy()
    sub_df = sub_df[sub_df['Direction'] == direction]

    reloc_coords = [0, 20]
    if country_list:
        sub_df = sub_df[sub_df['Country'].isin(country_list)]
        reloc_row = sub_df[sub_df['Country'] == country_list[-1]].head(1)
        reloc_coords = [reloc_row.iloc[0]['Long'], reloc_row.iloc[0]['Lat']]

    sub_df = sub_df[
        (sub_df.Month.str[0:4] >= str(rangeBar[0])) & (sub_df.Month.str[0:4] <= str(int(str(rangeBar[1]))))]
    sub_df = sub_df[sub_df['Irish Airport'] == irish_airport]

    grouped_df = sub_df.groupby(['Airport_code', 'Foreign Airport', 'Country', 'Long', 'Lat'], as_index=False)[
        'DATA'].sum()
    grouped_df = grouped_df[grouped_df['DATA'] != 0]

    trips_text = '{:,}'.format(sum(grouped_df['DATA']))

    if grouped_df.empty:
        fig_map = {}
    else:
        fig_map = px.scatter_mapbox(grouped_df, lat="Lat", lon="Long",
                                    color_continuous_scale=map_layouts[mapStyle]['color'],
                                    zoom=1 if reloc_coords[1] == 20 else 3,
                                    color="DATA",
                                    size=map_layouts[mapStyle]['size'],
                                    #height=350,
                                    hover_name=grouped_df['Foreign Airport'],
                                    center={'lon': reloc_coords[0], 'lat': reloc_coords[1]}
                                    )

        fig_map.update_layout(
            mapbox_style=map_layouts[mapStyle]['layout'],
            plot_bgcolor='GhostWhite',
            paper_bgcolor='GhostWhite',
            margin={"r": 0, "t": 0, "l": 0, "b": 0}
        )
        if mapStyle == 3:
            fig_map.update_layout(
                mapbox_style="white-bg",
                mapbox_layers=[
                    {
                        "below": 'traces',
                        "sourcetype": "raster",
                        "sourceattribution": "United States Geological Survey",
                        "source": [
                            "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                        ]
                    }
                ])

    # Filter top 10 for bar chart

    if grouped_df.empty:
        fig_bar = {}
        location_text = ''
    else:
        grouped_df.sort_values('DATA', inplace=True, ascending=False)
        top_10_df = grouped_df[0:10]
        location_text = top_10_df['Foreign Airport'].iloc[0]
        fig_bar = px.bar(top_10_df, x='Foreign Airport', y='DATA',
                         hover_data=['Foreign Airport', 'DATA'], opacity=1, color='DATA', log_y=bar_scales[bar_scale])
        fig_bar.update_layout(barmode='stack',
                              xaxis={'categoryorder': 'total descending'},
                              plot_bgcolor='GhostWhite',
                              paper_bgcolor='GhostWhite'
                              )
        fig_bar.update_xaxes(title='')

    if rangeBar[0] == rangeBar[1]:
        bar_text = 'Top ' + direction + ' destinations for ' + irish_airports_dict[
            irish_airport] + ' airport in ' + str(rangeBar[0])
        time_text = str(rangeBar[0])
    else:
        bar_text = 'Top ' + direction + ' destinations for ' + irish_airports_dict[
            irish_airport] + ' airport from ' + str(
            rangeBar[0]) + ' to ' + str(rangeBar[1])
        time_text = str(rangeBar[0]) + ' to ' + str(rangeBar[1])
    map_text = direction + ' passenger movement from ' + irish_airports_dict[irish_airport] + ' Airport'

    yearly_df = sub_df.copy()
    yearly_df['Year'] = yearly_df.Month.str[0:4]

    return fig_map, fig_bar, bar_text, map_text, time_text, trips_text, location_text

if __name__ == '__main__':
    app.run_server(debug=True)