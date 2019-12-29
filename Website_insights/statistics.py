import pandas as pd
import numpy as np
import warnings
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
from Website_insights.colors import *


def multipl_bar_chart(id, nb, graph_x, graph_y, names, colors, style_colors=chose_colors(), barmode='stack', x_label='', y_label='', y_label2=''):
    """plot a graph with multipl bar chart

    in :
    id :            id of the chart
    nb :            number of chart that have to be plot
    graph_x :       list of the x axis, length must be nb
    graph_y :       list of the y axis, length must be nb
    names :         list of the graph name, length must be nb
    colors :        list of the graph color, length must be nb
    style_colors :  dict of the style colors, default=chose_colors()
    barmode :       barmodeof the chart, default='stack' (['stack', 'group', 'overlay', 'relative'])
    x_label :       x label of the grouped chart, default=''
    y_label :       y label of the grouped chart, default=''
    y_label :       second y label of the grouped chart, default=''

    return :
    graph
    """
    graph = dcc.Graph(
            id=id,
            className='col-6',
            # set the style
            style={
                'min-height': '45vh',
                'min-width': '100vh',
                'backgroundColor': style_colors['background'],
                'color': style_colors['color'],
            },
            figure={
                # first the data we use for the graph
                "data": [
                    go.Bar(
                        x=graph_x[i],
                        y=graph_y[i],
                        name=names[i],
                        marker=dict(color = colors[i]))
                    for i in range(nb)],

                # after that you give the parameters for showing the graph in the right way
                "layout": go.Layout(
                    barmode=barmode,
                    xaxis=dict(
                        title=x_label
                    ),
                    yaxis=dict(
                        title=y_label
                    ),
                    plot_bgcolor = style_colors['background'],
                    paper_bgcolor = style_colors['background'],
                    font = {'color':  style_colors['color']}
                ),
            },
        ),
    return graph




def multipl_scatter_chart(id, nb, graph_x, graph_y, names, colors, style_colors=chose_colors(), x_label='', y_label='', y_label2=''):
    """plot a graph with multipl scatter chart

    in :
    id :            id of the chart
    nb :            number of chart that have to be plot
    graph_x :       list of the x axis, length must be nb
    graph_y :       list of the y axis, length must be nb
    names :         list of the graph name, length must be nb
    colors :        list of the graph color, length must be nb
    style_colors :  dict of the style colors, default=chose_colors()
    x_label :       x label of the grouped chart, default=''
    y_label :       y label of the grouped chart, default=''
    y_label :       second y label of the grouped chart, default=''

    return :
    graph
    """
    graph = dcc.Graph(
            id=id,
            className='col-6',
            # set the style
            style={
                'min-height': '45vh',
                'min-width': '100vh',
                'backgroundColor': style_colors['background'],
                'color': style_colors['color'],
            },
            figure={
                # first the data we use for the graph
                "data": [
                    go.Scatter(
                        x=graph_x[i],
                        y=graph_y[i],
                        name=names[i],
                        mode='markers',
                        marker=dict(color = colors[i]))
                    for i in range(nb)],

                # after that you give the parameters for showing the graph in the right way
                "layout": go.Layout(
                    yaxis=dict(
                        title=y_label
                    ),
                    # specify the second Y-axis for using 2 Y-axis in one plot
                    yaxis2=dict(
                        title=y_label2,
                        overlaying='y',
                        side='right',
                    ),
                    xaxis=dict(
                        title=x_label
                    ),
                    plot_bgcolor=style_colors['background'],
                    paper_bgcolor=style_colors['background'],
                    font={'color': style_colors['color']}
                ),
            },
        ),
    return graph






def alarmdescription(Dataset, description, style_colors=chose_colors()):
    """make the description of the most common {warningfault} description for {devices}

    in :
    Dataset :       dataset to use, dataset
    warningfault :  type of data showed by the graph, 'FAULT', 'WARNING', or 'NORMAL'
    device :        the device studied
    style_colors :  dict of the style colors, default=chose_colors()

    return :
    graph :         graph showing the 15 most common {warningfault} description for the {devices}
    """
    # look for the right values and prepare them for using in the graphs
    system = Dataset.loc[Dataset['description'] == description]
    # device1 = system.loc[Dataset['device'] == device]
    
    description = system.groupby('description').nunique().drop(columns=['description']).reset_index()
    description = description.sort_values(by=['DATE'], ascending=False).reset_index().drop(columns=['index'])
    # pick the highest 15 for best view of the description. Otherwise you can't read the description
    description = description[:15]

    # if there is no description available, this message will reveal, otherwise it will continue
    if description.empty :# == True:
        return html.P('There are no descriptions available for ',  '')
    else:
        # double return. One with the variable text, and the other the graph itself
        return  html.Div(className='col-3', style={'min-width': '100vh'}, children=[
                html.H5('This bar plot shows you the most common {warningfault} description for {devices}'
                    .format(warningfault=description)),
                html.P('This means that the top 15 description for the device are shown here. You can see what the most common {warningfault} is.'
                    .format(warningfault=description)),
        ]), \
            dcc.Graph(
                id='alarmdescription',
                className='col-6',
                style={
                    'min-height': '45vh',
                    'min-width': '100vh',
                    'backgroundColor': style_colors['background'],
                    'color': style_colors['color'],
                },
                figure={
                    # first the data we use for the graph
                    "data": [
                        go.Bar(
                            x=description['description'],
                            y=description['DATE'],
                            name='Description',
                            marker=dict(
                                color = style_colors['block1'],
                            ),
                            # orientation='h'
                        ),
                    ],

                    # after that you give the parameters for showing the graph in the right way
                    "layout": go.Layout(
                        yaxis=dict(
                            title='# of times logged'
                        ),
                        plot_bgcolor = style_colors['background'],
                        paper_bgcolor = style_colors['background'],
                        font = {'color': style_colors['color']}
                    ),
                },
            ),

def pie_chart(id, label, value, names, colors, style_colors=chose_colors()):
    """ make the plot of a pie graph

    in :
    id :            id of the chart, str
    label :         labels for the graph, dataframe
    value :         values for the graph, dataframe
    names :         graph name, str
    colors :        list of the graph color
    style_colors :  dict of the style colors, default=chose_colors()

    return :
    graph :         the graph himself
    """
    graph = dcc.Graph(
            id=id,
            className='col-6',
            style={
                'min-height': '45vh',
                'min-width': '100vh',
                'backgroundColor': style_colors['backgroundDiv'],
                'color': style_colors['color'],
            },
            figure={
                # first the data we use for the graph
                "data": [
                    go.Pie(
                        labels=label,
                        values=value,
                        name=names,
                        hoverinfo='label + value',
                        marker=dict(
                            colors=colors,
                        ),
                        hole=.4,
                    ),
                ],

                # after that you give the parameters for showing the graph in the right way
                "layout": go.Layout(
                    plot_bgcolor=style_colors['backgroundDiv'],
                    paper_bgcolor=style_colors['backgroundDiv'],
                    font={'color': style_colors['color']}
                ),
            },
        )
    return graph
