import pandas as pd
import numpy as np
import warnings
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import datetime as dt
import dash_table


def chose_colors(background='#171c31', background2='#1F2438', backgroundDiv='#1F2438', color='#aeadaf', white='#ffffff',
                 line1='#B8E986', line2='#EA6475', line3='#98CCD3', line4='#774898', line5='#DE4383', line6='#B38D6B',
                 block1='#3998AB', block2='#F3AE4B',
                 piePlot=['#B8E986', '#EA6475', '#98CCD3', '#774898', '#DE4383', '#B38D6B', '#3998AB', '#F3AE4B']):
    """permit to chose the color for the plots

    'background':   default='#1F2438',
    'background2':  default='#171C31',
    'backgroundDiv':default='#282D38',
    'color':        default='#aeadaf',
    'white':        default='#ffffff',
    'line1':        default='#B8E986',
    'line2':        default='#EA6475',
    'line3':        default='#98CCD3',
    'line4':        default='#774898',
    'line5':        default='#DE4383',
    'line6':        default='#B38D6B',
    'block1':       default='#3998AB',
    'block2':       default='#F3AE4B',
    'piePlot':      default=['#B8E986','#EA6475','#98CCD3', '#774898','#DE4383','#B38D6B','#3998AB','#F3AE4B']
    """
    colors = {'background': background,
              'background2': background2,
              'backgroundDiv': backgroundDiv,
              'color': color,
              'white': white,
              'line1': line1,
              'line2': line2,
              'line3': line3,
              'line4': line4,
              'line5': line5,
              'line6': line6,
              'block1': block1,
              'block2': block2,
              'piePlot': piePlot}
    return (colors)


def get_year(dataset, date):
    """get the year fromat date format ddmmyyyy

    in :
    dataset :   dataset where the dates come from
    date :      dates, dataframe

    return :
    years :     years, dataframe
    """
    dataset['years'] = (dataset[date] % 10 ** 4).astype(int)
    # return(['years'])


def get_quarter(dataset, date):
    """get the quarter fromat date format ddmmyyyy

        in :
        dataset :   dataset where the dates come from
        date :      dates, dataframe

        return :
        quarter :     quarter, dataframe
        """
    dataset['quarter'] = (dataset[date] // 10 ** 4 % 100 // 3 * 3).astype(int)


def get_month(dataset, date):
    """get the month fromat date format ddmmyyyy

    in :
    dataset :   dataset where the dates come from
    date :      dates, dataframe

    return :
    month :     month, dataframe
    """
    dataset['month'] = (dataset[date] % 10 ** 6 // 10000).astype(int)
    # return(['month'])


def get_day(dataset, date):
    """get the day fromat date format ddmmyyyy

    in :
    dataset :   dataset where the dates come from
    date :      dates, dataframe

    return :
    day :       day, dataframe
    """
    dataset['day'] = (dataset[date] // 10 ** 6).astype(int)
    return dataset['day']
    # return(['day'])


def get_weeks(dataset, date):
    """get the day fromat date format ddmmyyyy

    in :
    dataset :   dataset where the dates come from
    date :      dates, dataframe

    return :
    day :       day, dataframe
    """
    dataset['weeks'] = (dataset[date]//10**6 // 7 +1).astype(int)
    # return(['day'])

def get_duration(dataset, start_date, end_date):
    """get the period of time that a course take
        """
    date =(dataset[end_date] - dataset[start_date]).astype(int)
    dataset['duration'] = change_duration_format(date)

def change_duration_format(date):
    changed_date = ((date * 10 ** -4)*365 + (date % 10 ** 4 / 100)*30 + (date % 10 ** 2)).astype(int)
    return changed_date


def change_format(date):
    """change the format from aaaammjj to aaaa-mm-jj

    in :
    date :      dates dataframe (dataset[data])

    return :
    date :      dates dataframe (format : aaaa-mm-jj)
    """
    return (date % 10 ** 4).astype(str) + '-' + (date % 10 ** 6 // 10**4).astype(str) \
           + '-' + (date // 10 ** 6).astype(str)

    # (date % 10 ** 4).astype(int).astype(str)    : give aaaa
    # (date % 10 ** 6 // 10**4).astype(int).astype(str) : give mm
    # date // 10 ** 6).astype(int).astype(str)     : give jj

