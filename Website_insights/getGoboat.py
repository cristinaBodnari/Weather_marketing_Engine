from Website_insights.plots_statistics import *
from Website_insights.toolbox import *
from Website_insights.statistics import pie_chart

column = ['Direct', 'Email', 'Organic_Search', 'Paid_search', 'Referral', 'Social']


def getGoboat(dataset, colors):
    Low_High_Channel = html.Div(pie_chart(
        id='Low_High_Channel',
        label=formating_text_for_pie(dataset, 'Low, High', column),
        value=formating_text_for_pie(dataset, 'Low, High', column),
        names='Low_High_Channel',
        colors=[colors['block1']],

    ))

    Low_High_Age = html.Div(pie_chart(
        id='Low_High_Age',
        label=formating_text_for_pie(dataset, 'Low, High', column),
        value=formating_text_for_pie(dataset, 'Low, High', column),
        names='Low_High_Age',
        colors=[colors['block1']],

    ))

    Low_High_Campaigns = html.Div(pie_chart(
        id='Low_High_Campaigns',
        label=formating_text_for_pie(dataset, 'Low, High', column),
        value=formating_text_for_pie(dataset, 'Low, High', column),
        names='Low_High_Campaigns',
        colors=[colors['block1']],

    ))

    Low_High_Interests = html.Div(pie_chart(
        id='Low_High_Interests',
        label=formating_text_for_pie(dataset, 'Low, High', column),
        value=formating_text_for_pie(dataset, 'Low, High', column),
        names='Low_High_Interests',
        colors=[colors['block1']],

    ))

    Low_High_Language = html.Div(pie_chart(
        id='Low_High_Language',
        label=formating_text_for_pie(dataset, 'Low, High', column),
        value=formating_text_for_pie(dataset, 'Low, High', column),
        names='Low_High_Language',
        colors=[colors['block1']],

    ))

    Low_Medium_Channel = html.Div(pie_chart(
        id='Low_Medium_Channel ',
        label=formating_text_for_pie(dataset, 'Low, Medium', column),
        value=formating_text_for_pie(dataset, 'Low, Medium', column),
        names='Low_Medium_Channel ',
        colors=[colors['block1']],

    ))

    Low_Medium_Age = html.Div(pie_chart(
        id='Low_Medium_Age',
        label=formating_text_for_pie(dataset, 'Low, Medium', column),
        value=formating_text_for_pie(dataset, 'Low, Medium', column),
        names='Low_Medium_Age',
        colors=[colors['block1']],

    ))

    Low_Medium_Campaigns = html.Div(pie_chart(
        id='Low_Medium_Campaigns',
        label=formating_text_for_pie(dataset, 'Low, Medium', column),
        value=formating_text_for_pie(dataset, 'Low, Medium', column),
        names='Low_Medium_Campaigns',
        colors=[colors['block1']],

    ))

    Low_Medium_Interests = html.Div(pie_chart(
        id='Low_Medium_Interests',
        label=formating_text_for_pie(dataset, 'Low, Medium', column),
        value=formating_text_for_pie(dataset, 'Low, Medium', column),
        names='Low_Medium_Interests',
        colors=[colors['block1']],

    ))

    Low_Medium_Language = html.Div(pie_chart(
        id='Low_Medium_Language',
        label=formating_text_for_pie(dataset, 'Low, Medium', column),
        value=formating_text_for_pie(dataset, 'Low, Medium', column),
        names='Low_Medium_Language',
        colors=[colors['block1']],

    ))

    Low_Low_Channel = html.Div(pie_chart(
        id='Low_Low_Channel',
        label=formating_text_for_pie(dataset, 'Low, Low', column),
        value=formating_text_for_pie(dataset, 'Low, Low', column),
        names='Low_Low_Channel',
        colors=[colors['block1']],

    ))

    Low_Low_Age = html.Div(pie_chart(
        id='Low_Low_Age ',
        label=formating_text_for_pie(dataset, 'Low, Low', column),
        value=formating_text_for_pie(dataset, 'Low, Low', column),
        names='Low_Low_Age ',
        colors=[colors['block1']],

    ))

    Low_Low_Campaigns = html.Div(pie_chart(
        id='Low_Low_Campaigns',
        label=formating_text_for_pie(dataset, 'Low, Low', column),
        value=formating_text_for_pie(dataset, 'Low, Low', column),
        names='Low_Low_Campaigns',
        colors=[colors['block1']],

    ))

    Low_Low_Interests = html.Div(pie_chart(
        id='Low_Low_Interests ',
        label=formating_text_for_pie(dataset, 'Low, Low', column),
        value=formating_text_for_pie(dataset, 'Low, Low', column),
        names='Low_Low_Interests ',
        colors=[colors['block1']],

    ))

    Low_Low_Language = html.Div(pie_chart(
        id='Low_Low_Language',
        label=formating_text_for_pie(dataset, 'Low, Low', column),
        value=formating_text_for_pie(dataset, 'Low, HLow', column),
        names='Low_Low_Language',
        colors=[colors['block1']],

    ))

    High_Low_Channel = html.Div(pie_chart(
        id='High_Low_Channel',
        label=formating_text_for_pie(dataset, 'High, Low', column),
        value=formating_text_for_pie(dataset, 'High, Low', column),
        names='High_Low_Channel',
        colors=[colors['block1']],

    ))

    High_Low_Age = html.Div(pie_chart(
        id='High_Low_Age',
        label=formating_text_for_pie(dataset, 'High, Low', column),
        value=formating_text_for_pie(dataset, 'High, Low', column),
        names='High_Low_Age',
        colors=[colors['block1']],

    ))

    High_Low_Campaigns = html.Div(pie_chart(
        id='High_Low_Campaigns',
        label=formating_text_for_pie(dataset, 'High, Low', column),
        value=formating_text_for_pie(dataset, 'High, Low', column),
        names='High_Low_Campaigns',
        colors=[colors['block1']],

    ))

    High_Low_Interests = html.Div(pie_chart(
        id='High_Low_Interests',
        label=formating_text_for_pie(dataset, 'High, Low', column),
        value=formating_text_for_pie(dataset, 'High, Low', column),
        names='High_Low_Interests',
        colors=[colors['block1']],

    ))

    High_Low_Language = html.Div(pie_chart(
        id='High_Low_Language',
        label=formating_text_for_pie(dataset, 'High, Low', column),
        value=formating_text_for_pie(dataset, 'High, Low', column),
        names='High_Low_Language',
        colors=[colors['block1']],

    ))

    High_Medium_Channel = html.Div(pie_chart(
        id='High_Medium_Channel',
        label=formating_text_for_pie(dataset, 'High, Medium', column),
        value=formating_text_for_pie(dataset, 'High, Medium', column),
        names='High_Medium_Channel',
        colors=[colors['block1']],

    ))

    High_Medium_Age = html.Div(pie_chart(
        id='High_Medium_Age',
        label=formating_text_for_pie(dataset, 'High, Medium', column),
        value=formating_text_for_pie(dataset, 'High, Medium', column),
        names='High_Medium_Age',
        colors=[colors['block1']],

    ))

    High_Medium_Campaigns = html.Div(pie_chart(
        id='High_Medium_Campaigns',
        label=formating_text_for_pie(dataset, 'High, Medium', column),
        value=formating_text_for_pie(dataset, 'High, Medium', column),
        names='High_Medium_Campaigns',
        colors=[colors['block1']],

    ))

    High_Medium_Interests = html.Div(pie_chart(
        id='High_Medium_Interests',
        label=formating_text_for_pie(dataset, 'High, Medium', column),
        value=formating_text_for_pie(dataset, 'High, Medium', column),
        names='High_Medium_Interests',
        colors=[colors['block1']],

    ))

    High_Medium_Language = html.Div(pie_chart(
        id='High_Medium_Language',
        label=formating_text_for_pie(dataset, 'High, Medium', column),
        value=formating_text_for_pie(dataset, 'High, Medium', column),
        names='High_Medium_Language',
        colors=[colors['block1']],

    ))

    High_High_Channel = html.Div(pie_chart(
        id='High_High_Channel',
        label=formating_text_for_pie(dataset, 'High, High', column),
        value=formating_text_for_pie(dataset, 'High, High', column),
        names='High_High_Channel',
        colors=[colors['block1']],

    ))

    High_High_Age = html.Div(pie_chart(
        id='High_High_Age',
        label=formating_text_for_pie(dataset, 'High, High', column),
        value=formating_text_for_pie(dataset, 'High, High', column),
        names='High_High_Age',
        colors=[colors['block1']],

    ))

    High_High_Campaigns = html.Div(pie_chart(
        id='High_High_Campaigns',
        label=formating_text_for_pie(dataset, 'High, High', column),
        value=formating_text_for_pie(dataset, 'High, High', column),
        names='High_High_Campaigns',
        colors=[colors['block1']],

    ))

    High_High_Interests = html.Div(pie_chart(
        id='High_High_Interests',
        label=formating_text_for_pie(dataset, 'High, High', column),
        value=formating_text_for_pie(dataset, 'High, High', column),
        names='High_High_Interests',
        colors=[colors['block1']],

    ))

    High_High_Language = html.Div(pie_chart(
        id='High_High_Language',
        label=formating_text_for_pie(dataset, 'High, High', column),
        value=formating_text_for_pie(dataset, 'High, High', column),
        names='High_High_Language',
        colors=[colors['block1']],

    ))

    return html.Div(id='stat-graphs', className='container-fluid', children=[
        html.Div(className='row', children=[
            Low_High_Age,
            Low_High_Campaigns,
            Low_High_Channel,
            Low_High_Interests,
            Low_High_Language,
            Low_Medium_Age,
            Low_Medium_Campaigns,
            Low_Medium_Channel,
            Low_Medium_Interests,
            Low_Medium_Language,
            Low_Low_Age,
            Low_Low_Campaigns,
            Low_Low_Channel,
            Low_Low_Interests,
            Low_Low_Language,
            High_Low_Age,
            High_Low_Campaigns,
            High_Low_Channel,
            High_Low_Interests,
            High_Low_Language,
            High_Medium_Age,
            High_Medium_Campaigns,
            High_Medium_Channel,
            High_Medium_Interests,
            High_Medium_Language,
            High_High_Age,
            High_High_Campaigns,
            High_High_Channel,
            High_High_Interests,
            High_High_Language,
        ]), html.Br()])
