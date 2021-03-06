# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

from main import container
from dataset.data import data

from charts.recommendation import Recommendation

external_stylesheets = [
    # dbc.themes.BOOTSTRAP,
    {
        'href': 'https://fonts.googleapis.com/icon?family=Material+Icons',
        'rel': 'stylesheet'
    },
    {
        'rel': "preconnect",
        'href': "https://fonts.gstatic.com"
    },
    {
        'href': "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
        'rel': "stylesheet"
    }
]
app = dash.Dash(__name__, prevent_initial_callbacks=True,
                external_stylesheets=external_stylesheets)

app.layout = container.layout

# interactive bar chart


@app.callback(
    Output(component_id='bar_graph2', component_property='figure'),
    [Input(component_id='bar_dropdown1', component_property='value'), Input(component_id='bar_dropdown2',
                                                                            component_property='value'), Input(component_id='bar_dropdown3', component_property='value')]
)
def update_barchart(selected_value1, selected_value2, selected_value3):
    nutrients = selected_value3
    recipes = [selected_value1, selected_value2]

    nutrients_df = data.nutrients_df
    daily_nutrients_intake = dict(
        zip(nutrients_df['nutrients'], nutrients_df['value']))

    daily_dose = []
    for x in nutrients:
        if(x.endswith('mg')):
            daily_dose.append(daily_nutrients_intake[x]/1000)
        else:
            daily_dose.append(daily_nutrients_intake[x])

    recipe_nutrients = []
    for x in recipes:
        recipe_data = data.df[data.df['name'] == x]
        temp = []
        for y in nutrients:
            if y == ' ':
                temp.append(0.0)
            elif(y.endswith('mg')):
                temp.append(float(recipe_data[y].to_string(index=False))/1000)
            else:
                temp.append(float(recipe_data[y].to_string(index=False)))
        temp = [float(i) for i in temp]
        recipe_nutrients.append(temp)

    figure = go.Figure(data=[
        go.Bar(name=recipes[0], x=nutrients, y=recipe_nutrients[0]),
        go.Bar(name=recipes[1], x=nutrients, y=recipe_nutrients[1]),
        go.Bar(name='daily intake', x=nutrients, y=daily_dose)
    ])

    return figure


@app.callback(
    Output(component_id='alternate_recipes', component_property='children'),
    Input(component_id='bar_dropdown7', component_property='value')
)
def recommend_alternative(value):
    sim_recipes, current_details = Recommendation.score_cal(value)
    sim_list = sim_recipes.values.tolist()

    sim_recipe_list = []

    table_header = [
        html.Thead(html.Tr([html.Th("Rank"), html.Th("Recipe"),
                   html.Th("Rating"), html.Th("Calories"), ]))
    ]

    for i, x in enumerate(sim_list):
        sim_recipe_list.append(
            html.Tr([
                html.Td(i+1),
                html.Td(html.A(x[0], href=x[1])),
                html.Td(x[2]),
                html.Td(x[3]),
            ])
        )

    table_body = [html.Tbody(sim_recipe_list)]

    table = html.Div([
        html.P("{0} rated {1} and has {2} calories".format(
            value, current_details[0], current_details[1])),

        dbc.Table(table_header + table_body, bordered=False)
    ])

    return table


if __name__ == '__main__':
    app.run_server(debug=True)
