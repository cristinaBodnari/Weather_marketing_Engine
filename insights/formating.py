import pandas as pd
import numpy as np
import warnings
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import datetime as dt
import dash_table


def formating_text_for_bar(Dataset,  sortedby,groupedby, nb_see=10):
    """formating data for bar chart (text type)

    in :
    Dataset :       dataset to plot, dataset
    groupedby :     for the groupby function, str
    sortedby :      for the sort_values function, str
    nb_see :        number of data show by the graph, default=15

    return :
    data :          formated data
    """
    data = Dataset.sort_values(by=sortedby, ascending=False).reset_index().drop(columns=['index'])

    data = data.groupby([pd.Grouper(key=groupedby)]).sum().reset_index()

    # data = data.sort_values(by=sortedby, ascending=False).reset_index().drop(columns=['index'])



    return data


def formating_text_for_pie(Dataset, groupedby, sortedby):
    """formating data for pie chart (text type)

    in :
    Dataset :       dataset to plot, dataset
    groupedby :     for the groupby function, str
    sortedby :      for the sort_values function, str
    nb_see :        number of data show by the graph, default=15

    return :
    data :          formated data
    """

    data = Dataset.groupby(groupedby).count()
    data = data.groupby([pd.Grouper(key=groupedby, freq='w')]).sum().reset_index()

    # data = data.sort_values(by=sortedby, ascending=False).sum().reset_index()
    # data[groupedby] = data[groupedby].replace(r'\s+', np.nan, regex=True)
    #
    # data[groupedby] = data[groupedby].fillna('Unknown')

    return (data)






def formating_age_for_pie(Dataset, dates1, dates2):
    """formating data for pie chart (periode range type)

    in :
    Dataset :       dataset to plot, dataset
    dates1 :        beginigs of the periode dates, format : 2019-04-09, dataframe
    dates2 :        ends of the periode dates, format : 2019-04-09, dataframe

    return :
    dico_age :      periode range dict
    """
    Dataset = Dataset.dropna().reset_index()

    Dataset['temp'] = (pd.to_datetime(dates1) - pd.to_datetime(dates2)) / 365.25
    Dataset['age'] = Dataset['temp'].astype('str').str.split('days').str[0]
    Dataset = Dataset.drop(columns='temp')

    Dataset = Dataset.sort_values(by=['age'], ascending=False).reset_index().drop(columns=['index'])
    Dataset['age'] = Dataset['age'].astype('int')

    tens = Dataset.groupby([Dataset['age'] <= 20]).count().drop(columns=['age']).reset_index()
    twenty = Dataset.groupby([Dataset['age'].between(20, 30)]).count().drop(columns=['age']).reset_index()
    thirty = Dataset.groupby([Dataset['age'].between(30, 40)]).count().drop(columns=['age']).reset_index()
    fourty = Dataset.groupby([Dataset['age'].between(40, 50)]).count().drop(columns=['age']).reset_index()
    fifty = Dataset.groupby([Dataset['age'].between(50, 60)]).count().drop(columns=['age']).reset_index()
    sixtyplus = Dataset.groupby([Dataset['age'] >= 60]).count().drop(columns=['age']).reset_index()

    dico_age = {'<20': tens['firstName'][1],
                '20-30': twenty['firstName'][1],
                '30-40': thirty['firstName'][1],
                '40-50': fourty['firstName'][1],
                '50-60': fifty['firstName'][1],
                '>60': sixtyplus['firstName'][1]}

    return dico_age


def percentage(Dataset, columns, r_nb=2):
    """calculate the purcentage for some data

    in :
    Dataset :       dataset to use, dataset
    columuns :      column on which the purcentage will be calculated, list of columns
    r_nb :          number of number after the comma for the round function, int, default=2

    return :
    count :         the purcentage of row containing no NaN in the columns selected, float
    """
    total = Dataset.shape[0]
    count = Dataset[columns].dropna(subset=columns).count()
    count = count * 100 / total
    return round(count[0], r_nb)