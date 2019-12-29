import pandas as pd
import numpy as np
import warnings
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
from formating import *
from statistics import *


# here are all the functions that are normal statistics called from other files
def getStatBWTS(dataset,colors):
    """plot the statistics graph
    in :
    dataset1 :  "techcross_componentactivity.csv"
    dataset2 :  "techcross_ballast_deballast.csv"
    dataset3 :  "techcross_measurescomponents.csv"
    colors :    colors dictonary
    """


    Session_All_traffic_legend = html.Div(className='col-3', style={'min-width': '100vh'}, children=[
        html.H5('All traffic')
    ])


    Session_All_traffic = html.Div(multipl_bar_chart(
        id='Unique last names',
        nb=1,
        graph_x=[formating_text_for_bar(dataset, 'Rainfall' ,'Session_All_traffic')['Rainfall']],
        graph_y=[formating_text_for_bar(dataset, 'Rainfall' ,'Session_All_traffic')['Session_All_traffic']],
        names='Unique last names',
        colors=[colors['block1']],
        barmode='stack',
        x_label='',
        y_label='# of times registered in dataset',
        y_label2='', ))

    Click_Channels_legend = html.Div(className='col-3', style={'min-width': '100vh'}, children=[
        html.H5('Channels')
    ])

    Click_Channels = html.Div(multipl_bar_chart(
        id='Unique ',
        nb=1,
        graph_x=[formating_text_for_bar(dataset, 'Rainfall','Click_Channels')['Rainfall']],
        graph_y=[formating_text_for_bar(dataset, 'Rainfall','Click_Channels')['Click_Channels']],
        names='Unique last names',
        colors=[colors['block1']],
        barmode='stack',
        x_label='',
        y_label='# of times registered in dataset',
        y_label2='', ))

    Session_Traffic_Campaign_legend = html.Div(className='col-3', style={'min-width': '100vh'}, children=[
        html.H5('Traffic Campaign')
    ])

    Session_Traffic_Campaign = html.Div(multipl_bar_chart(
        id='Unique 1',
        nb=1,
        graph_x=[formating_text_for_bar(dataset, 'Rainfall','Session_Traffic_Campaign')['Rainfall']],
        graph_y=[formating_text_for_bar(dataset, 'Rainfall','Session_Traffic_Campaign')['Session_Traffic_Campaign']],
        names='Unique last names',
        colors=[colors['block1']],
        barmode='stack',
        x_label='',
        y_label='# of times registered in dataset',
        y_label2='', ))









    Session_Ads_campaign_legend = html.Div(className='col-3', style={'min-width': '100vh'}, children=[
        html.H5('Ads campaign')
    ])

    Session_Ads_campaign = html.Div(multipl_bar_chart(
        id='Unique 2',
        nb=1,
        graph_x=[formating_text_for_bar(dataset, 'Rainfall', 'Session_Ads_campaign', 'Rainfall')['Rainfall']],
        graph_y=[formating_text_for_bar(dataset, 'Rainfall','Session_Ads_campaign')['Session_Ads_campaign']],
        names='Unique last names',
        colors=[colors['block1']],
        barmode='stack',
        x_label='',
        y_label='# of times registered in dataset',
        y_label2='', ))

    Click_Ads_bid_Adjustments_Legend = html.Div(className='col-3', style={'min-width': '100vh'}, children=[
        html.H5('Ads bid Adjustments')
    ])

    Click_Ads_bid_Adjustments = html.Div(multipl_bar_chart(
        id='Unique 3',
        nb=1,
        graph_x=[formating_text_for_bar(dataset, 'Rainfall','Click_Ads-bid_Adjustments')['Rainfall']],
        graph_y=[formating_text_for_bar(dataset, 'Rainfall','Click_Ads-bid_Adjustments')['Click_Ads-bid_Adjustments']],
        names='Unique last names',
        colors=[colors['block1']],
        barmode='stack',
        x_label='',
        y_label='# of times registered in dataset',
        y_label2='', ))

    Click_Sitelinks_legend = html.Div(className='col-3', style={'min-width': '100vh'}, children=[
        html.H5('Site links')
    ])

    Click_Sitelinks = html.Div(multipl_bar_chart(
        id='Unique 4',
        nb=1,
        graph_x=[formating_text_for_bar(dataset, 'Rainfall','Click_Sitelinks')['Rainfall']],
        graph_y=[formating_text_for_bar(dataset, 'Rainfall','Click_Sitelinks')['Click_Sitelinks']],
        names='Unique last names',
        colors=[colors['block1']],
        barmode='stack',
        x_label='',
        y_label='# of times registered in dataset',
        y_label2='', ))




    return html.Div(id='stat-graphs', className='container-fluid', children=[
        html.Div(className='row', children=[
            Session_All_traffic_legend,
            Session_All_traffic,
            Click_Channels_legend,
            Click_Channels,
            Session_Traffic_Campaign_legend,
            Session_Traffic_Campaign,
            Session_Ads_campaign_legend,
            Session_Ads_campaign,
            Click_Ads_bid_Adjustments_Legend,
            Click_Ads_bid_Adjustments,
            Click_Sitelinks_legend,
            Click_Sitelinks,



        ])
    ])
