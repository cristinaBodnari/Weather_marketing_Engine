import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_dangerously_set_inner_html
from Style import Style
from statistics import *
# from Extra_function import *
from formating import *
from getStatBWTS import *
from colors import *
import datetime
import pandas as pd
# warnings.filterwarnings('ignore')


# start up the Dash-board
if __name__ == '__main__':
    print(" ")
    print("|------------------------------|")
    print("|        debut de main         |")
    print("|------------------------------|")
    print(datetime.datetime.now())
    print(" ")

    #colors for the graph
    colors = chose_colors()

    #Dataset used
    Dataset = pd.read_csv('Dataset.csv',parse_dates=['Date'])


    # __name__ is for appending the CSS file in the "assets" folder
    app = dash.Dash(__name__)

    # append external css files
    app.css.append_css({
        "external_url": "https://p.w3layouts.com/demos_new/template_demo/07-04-2018/bake-demo_Free/1027606894/web/css/bootstrap.min.css"})
    app.css.append_css({
        "external_url": "https://p.w3layouts.com/demos_new/template_demo/07-04-2018/bake-demo_Free/1027606894/web/css/fontawesome-all.min.css"})
    app.css.append_css({
        "external_url": "https://p.w3layouts.com/demos_new/template_demo/07-04-2018/bake-demo_Free/1027606894/web/css/owl.carousel.css"})
    app.css.append_css({
        "external_url": "https://p.w3layouts.com/demos_new/template_demo/07-04-2018/bake-demo_Free/1027606894/web/css/style.css"})

    # setting up the layout of the Dash-board. So actually just the contents
    app.layout = html.Div(style={'backgroundColor': colors['background2'], 'color': '#774898'}, children=[ #color a changer
        # set header and css of dashboard
        html.Div([
            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                Style.getWebsiteCss("css.txt") + Style.getWebsiteHeader()),
        ]),
        # the contents of the HTML
        html.Div(className='container-fluid', children=[
            dcc.Dropdown(
                id='dropdown-graphs',
                style={'backgroundColor': colors['backgroundDiv'], 'color': colors['color']},
                options=[
                    {'label': 'Statistical', 'value': 'Stat'},
                ],
                # set standard value
                value='Stat',
            ),
            html.Div(id='output-container')
        ])
        ])

    # making a callback for an interactive and reactive dashboard
    @app.callback(
        dash.dependencies.Output('output-container', 'children'),
        [dash.dependencies.Input('dropdown-graphs', 'value')])
    def render_content(value):
        # making an if-statement for after selecting a value in the dropdown menu.Then he shows the graphs of that value
        if value == 'Stat':
            return html.Div(id='output-stat', children=[
                html.Div(getStatBWTS(Dataset,colors)),
                # html.Div(ballast_deballast_system_aw(Dataset1, Dataset2, Dataset3))
            ])
    # run it on the web-server
    app.run_server(debug=True)
