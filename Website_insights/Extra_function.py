import pandas as pd
import numpy as np
import warnings
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
from Website_insights.colors import *
# warnings.filterwarnings('ignore')
# from MySQL import *


# set the right colorscheme for the dashboard
# colors = {
#     'background': '#1F2438',
#     'color': '#aeadaf',
#     'line1': '#B8E986',
#     'line2': '#EA6475',
#     'line3': '#98CCD3',
#     'line4': '#774898',
#     'line5': '#DE4383',
#     'line6': '#B38D6B',
#     'block1': '#3998AB',
#     'block2': '#F3AE4B',
# }
#colors for the graph
colors = chose_colors()


def ballast_deballast_system_aw(dataset1, dataset2, dataset3): # ballast deballast warning alarm count
    alarm = dataset1.loc[dataset1['level'] == 'FAULT']
    alarm_1 = alarm.groupby('device').nunique().drop(columns='device').reset_index()
    warning = dataset1.loc[dataset1['level'] == 'WARNING']
    warning_1 = warning.groupby('device').nunique().drop(columns='device').reset_index()

    # set up the Dash graph an its parameters
    def iter_(df,Count_list,devices): #je suis moyen sure de cette idee... :/
        if len(df)>0:
            for jj in range(len(devices)):
                for kk in range(len(df)):
                    if devices[jj] == df[kk]:
                        Count_list[jj] +=1

    devices=dataset1.device.unique() #string
    Count_A=np.array([0.0]*len(devices)) #Alarms
    Count_W=np.array([0.0]*len(devices)) #Warning

    EndTime_BD=[]
    for i in range(dataset2.shape[0]):
            start=str(dataset2.iloc[i,1])
            end  =str(dataset2.iloc[i,2])
            if start=='nan':
                pass
            else:
                EndTime_BD.append(start) #for later use
            try:
                d1=dataset1[start:end].copy()  #alarms inside the ballast deballast
                A=0
                d_f=(d1[d1['level']=='FAULT'].device.unique()) #inside ballast
                d_f_2=(d1[d1['level']=='WARNING'].device.unique()) #inside ballast
                iter_(d_f,Count_A,devices)
                iter_(d_f_2,Count_W,devices)

            except KeyError:
                pass

    Bd_alarm_device=pd.DataFrame(data={'device':devices,'Count':Count_A}) #ballast deballast
    Bd_alarm_device = Bd_alarm_device.sort_values(by=['Count'], ascending=False).reset_index().drop(columns=['index'])
    Bd_warning_device=pd.DataFrame(data={'device':devices,'Count':Count_W}) #ballast deballast
    Bd_warning_device = Bd_warning_device.sort_values(by=['Count'], ascending=False).reset_index().drop(columns=['index'])

    first = Bd_alarm_device['device'][0]
    last = Bd_warning_device['device'].iloc[-1]
    number1 = Bd_alarm_device['Count'][0]
    number2 = Bd_warning_device['Count'].iloc[-1]

    # double return. One with the variable text, and the other the graph itself
    return html.Div(className='col-3', style={'min-width': '100vh'}, children=[
        html.H5('This bar plot tells you the number of faults and warnings per device. This is only for the ballast'
                '/deballast process'),
        html.P('This means that you can see here how good your device (not) works. If a fault occur, the process stops.'
               'So the more faults you see, the more processes were shut before the process was finished.'
               'You can compare this graph to the graph in total. You can see how many faults/warnings from the '
               'total are ballast/deballast process. In that way you can see in a easy way where there bottleneck is '
               'You can see that {first} has the most faults({number1}). and {last} the most warnings ({number2})'.format(
                first=first, last=last, number1=number1, number2=number2)),
    ]), \
        dcc.Graph(
            id='184',
            className='col-6',
            style={
                'min-height': '45vh',
                'min-width': '100vh',
                'backgroundColor': colors['background'],
                'color': colors['color'],
            },
            figure={
                # first the data we use for the graph
                "data": [
                    go.Bar(
                        x=Bd_alarm_device['device'],
                        y=Bd_alarm_device['Count'],
                        name='Faults',
                        marker=dict(
                            color=colors['block1'],
                        )
                    ),

                    go.Bar(
                        x=Bd_warning_device['device'],
                        y=Bd_warning_device['Count'],
                        name='Warnings',
                        marker=dict(
                            color=colors['block2'],
                        )
                    )

                ],

                # after that you give the parameters for showing the graph in the right way
                "layout": go.Layout(
                    barmode='stack',
                    xaxis=dict(
                        title='Device'
                    ),
                    yaxis=dict(
                        title='# of times occured'
                    ),
                    plot_bgcolor=colors['background'],
                    paper_bgcolor=colors['background'],
                    font={'color': colors['color']}
                ),
            },
        ),
