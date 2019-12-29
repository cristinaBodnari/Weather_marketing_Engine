import pandas as pd
import numpy as np
import warnings
import dash
import dash_core_components as dcc
import plotly.graph_objs as go

from Website_insights.toolbox import *
from Website_insights.formatting_data import *


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
    barmode :       barmode of the chart, default='stack' (['stack', 'group', 'overlay', 'relative'])
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
                'backgroundColor': style_colors['backgroundDiv'],
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
                    plot_bgcolor=style_colors['backgroundDiv'],
                    paper_bgcolor=style_colors['backgroundDiv'],
                    font={'color': style_colors['color']
                            }
                ),
            },
        ),
    return graph



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
