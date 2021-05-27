import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from dataset.data import data

class BarChart2:
    nutrients = ['carbohydrates_g', 'sugars_g', 'fat_g']
    category = ['side-dish', 'breakfast-and-brunch']
    daily_nutrients_intake = {
        'carbohydrates_g' : 260,
        'sugars_g' : 90,
        'fat_g' : 70,
        'protein_g' : 50,
        'dietary_fiber_g' : 25,
        'sodium_mg' : 2300,
        'calcium_mg' : 1000,
        'iron_mg' : 14.8,
        'magnesium_mg' : 400,
        'potassium_mg' : 4700,
    }

    bar_data = data.df.groupby("category").agg({'name':'count',nutrients[0]:'mean',nutrients[1]:'mean',nutrients[2]:'mean'}).reset_index()
    bar_data = bar_data[bar_data['name']>100]

    category_nutrients = []

    for x in category:
        category_data = bar_data[bar_data['category']==x]
        temp = []
        for y in nutrients:
            temp.append(category_data[y].to_string(index=False))
        temp = [float(i) for i in temp]
        category_nutrients.append(temp)

    daily_dose = []
    for x in nutrients:
        if(x.endswith('mg')):
            daily_dose.append(daily_nutrients_intake[x]/1000)
        else: 
            daily_dose.append(daily_nutrients_intake[x])

    figure = go.Figure(data=[
        go.Bar(name=category[0], x=nutrients, y=category_nutrients[0]),
        go.Bar(name=category[1], x=nutrients, y=category_nutrients[1]),
        go.Bar(name='daily intake', x=nutrients, y=daily_dose)
    ])

    # Change the bar mode
    figure.update_layout(barmode='group')

    fig = html.Div(children=[
        html.Div(children=[
            dcc.Dropdown(
                id = 'bar_dropdown1',
                options = [
                    { 'label' : 'Main dish', 'value' : 'main-dish' },
                    { 'label' : 'Dessert', 'value' : 'desserts' },
                    { 'label' : 'Drinks', 'value' : 'drinks' },
                    { 'label' : 'Bread', 'value' : 'bread' },
                    { 'label' : 'Side dish', 'value' : 'side-dish' },
                    { 'label' : 'Breakfast and Brunch', 'value' : 'breakfast-and-brunch' },
                ],
                optionHeight = 25,
                value = 'side-dish',
                disabled = False,
                multi = False,
                searchable = True,
                search_value = '',
                placeholder = 'Select...',
                clearable = False,
                style = { 'width' : "95%" }
            ),
            dcc.Dropdown(
                id = 'bar_dropdown2',
                options = [
                    { 'label' : 'Main dish', 'value' : 'main-dish' },
                    { 'label' : 'Dessert', 'value' : 'desserts' },
                    { 'label' : 'Drinks', 'value' : 'drinks' },
                    { 'label' : 'Bread', 'value' : 'bread' },
                    { 'label' : 'Side dish', 'value' : 'side-dish' },
                    { 'label' : 'Breakfast and Brunch', 'value' : 'breakfast-and-brunch' },
                ],
                optionHeight = 25,
                value = 'breakfast-and-brunch',
                disabled = False,
                multi = False,
                searchable = True,
                search_value = '',
                placeholder = 'Select...',
                clearable = False,
                style = { 'width' : "95%" }
            ),
        ],className="row"),

        html.Br(),

        dcc.Dropdown(
            id = 'bar_dropdown3',
            options = [
                { 'label' : 'Carbohydrate', 'value' : 'carbohydrates_g'},
                { 'label' : 'Sugar', 'value' : 'sugars_g' },
                { 'label' : 'Fat', 'value' : 'fat_g' },
                { 'label' : 'Protein', 'value' : 'protein_g' },
                { 'label' : 'Fiber', 'value' : 'dietary_fiber_g' },
                { 'label' : 'Sodium', 'value' : 'sodium_mg' },
                { 'label' : 'Calcium', 'value' : 'calcium_mg'},
                { 'label' : 'Iron', 'value' : 'iron_mg'},
                { 'label' : 'Magnesium', 'value' : 'magnesium_mg'},
                { 'label' : 'Potassium', 'value' : 'potassium_mg'},
            ],
            optionHeight = 25,
            value = nutrients,
            disabled = False,
            multi = True,
            searchable = True,
            search_value = '',
            placeholder = 'Select...',
            clearable = False,
            style = { 'width' : "95%" }
        ),

        html.Br(),
        dcc.Graph(
            id='bar_graph2',
            figure=figure
        )
    ])