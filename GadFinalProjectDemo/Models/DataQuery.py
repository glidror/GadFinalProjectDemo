
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import base64
import datetime
import io
from os import path


def plot_case_1(df , start_date , end_date , kind):
    print("Running from plot_case_1()")
    rd = {}
    start_date_series = df['Start Date']
    ts = pd.to_datetime(start_date_series)
    df['Date'] = ts
    df = df.set_index('Date')
    df1 = df[str(end_date) : str(start_date)]
    series_approving = df1['Approving']
    if series_approving.empty:
        rd['isempty'] = 'empty'
        rd['img'] = ''
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        series_approving.plot(ax=ax,  kind = kind, title = 'Trump Approval Index', figsize = (15, 6), fontsize = 14, style = 'bo-')
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        rd['isempty'] = ''
        rd['img'] = pngImageB64String
        # return pngImageB64String
    return rd




def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

def covid19_day_ratio(df , countries , start_date , end_date):
    df1 = df.drop(['Lat' , 'Long' , 'Province/State'], 1)
    df1 = df1.rename(columns={'Country/Region': 'Country'})
    df1 = df1.groupby('Country').sum()
    df1 = df1.loc[ countries ]
    df1 = df1.transpose()
    df1.index = pd.to_datetime(df1.index)
    columns = list(df1)
    df2 = df1
    for col in columns:
        df2[col] = df1[col] / df1[col].shift(1)
    df2 = df2.replace([np.inf, -np.inf], np.nan)
    df2 = df2.fillna(value=0)
    df2 = df2[start_date : end_date]
    return df2


def Get_NormelizedWeatherDataset():
    dfw = pd.read_csv(path.join(path.dirname(__file__), "..\\static\\data\\weather_description.csv"))
    dff = pd.DataFrame(columns=list(['datetime', 'Weather', 'State']))
    for col in dfw.columns: 
        if (col != 'datetime'):
            dft = dfw[['datetime', col]].copy()
            dft['State'] = col
            dft = dft.rename(columns={col: 'Weather'})
            dff = dff.append(dft)
    return (dff)

def Get_NormelizedUFOTestmonials():
    df = pd.read_csv(path.join(path.dirname(__file__), "..\\static\\data\\UFOTestemonials.csv"))
    df1 = df.drop(['Event_URL' , 'Day' , 'Month', 'Year', 'Event_URL'], 1)
    df2 = Convert_StateCode_ToFullName(df1)
    df3 = df2.dropna()
    df3['Event_Time'] = pd.to_datetime(pd.Series(df3['Event_Time']), format='%Y-%m-%dT%H:%M:%SZ', errors = 'coerce')
    return df3


def Convert_StateCode_ToFullName(df):
    df_short_state = pd.read_csv(path.join(path.dirname(__file__), "..\\static\\data\\USStatesCodes.csv"))
    #df_short_state = df_short_state.set_index('Code')
    #df_short_state = df_short_state.sort_index()
    s = df_short_state.set_index('Code')['State']
    return (df.replace(s))

def get_states_choices():
    df_short_state = pd.read_csv(path.join(path.dirname(__file__), "..\\static\\data\\USStatesCodes.csv"))
    s = df_short_state.set_index('Code')['State']

    df1 = df_short_state.groupby('State').sum()
    l = df1.index
    m = list(zip(l , l))
    return m




def AlienVisitsSummery(df , States , start_date , end_date):
    df1 = df.drop(['Event_URL' , 'Day' , 'Month', 'Year'], 1)
    df1 = df1.rename(columns={'Country/Region': 'Country'})
    df1 = df1.groupby('Country').sum()
    df1 = df1.loc[ countries ]
    df1 = df1.transpose()
    df1.index = pd.to_datetime(df1.index)
    columns = list(df1)
    df2 = df1
    for col in columns:
        df2[col] = df1[col] / df1[col].shift(1)
    df2 = df2.replace([np.inf, -np.inf], np.nan)
    df2 = df2.fillna(value=0)
    df2 = df2[start_date : end_date]
    return df2

def get_countries_choices(df):
    df1 = df.rename(columns={'Country/Region': 'Country'})
    df1 = df1.groupby('Country').sum()
    l = df1.index
    m = list(zip(l , l))
    return m