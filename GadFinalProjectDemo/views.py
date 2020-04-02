"""
Project by: Gad Lidror (Demo)
Date: TASHAP
Grade: 10th grade, Tichonet

This file include all the redirections of the different pages, and thier routs
It has most of the logic of the project, written in Python, under Flask, WTF and more
"""
from GadFinalProjectDemo import app

import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.figure import Figure
import pandas as pd

import io
import base64
import json 
import requests

from flask     import Flask, render_template, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms   import Form, validators, ValidationError
from wtforms   import BooleanField, StringField, PasswordField, TextField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired


from wtforms.fields.html5 import DateField , DateTimeField



from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from datetime import datetime
from os       import path

# Integrate internal project models
# ---------------------------------
from GadFinalProjectDemo.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from GadFinalProjectDemo.Models.FormStructure import DataQueryFormStructure 
from GadFinalProjectDemo.Models.FormStructure import LoginFormStructure 
from GadFinalProjectDemo.Models.FormStructure import UserRegistrationFormStructure 
from GadFinalProjectDemo.Models.FormStructure import ExpandForm
from GadFinalProjectDemo.Models.FormStructure import CollapseForm
from GadFinalProjectDemo.Models.FormStructure import SinglePresidentForm
from GadFinalProjectDemo.Models.FormStructure import AllOfTheAboveForm
from GadFinalProjectDemo.Models.FormStructure import Covid19DayRatio

from GadFinalProjectDemo.Models.DataQuery     import plot_to_img
from GadFinalProjectDemo.Models.DataQuery     import Get_NormelizedUFOTestmonials
from GadFinalProjectDemo.Models.DataQuery     import get_states_choices
from GadFinalProjectDemo.Models.DataQuery     import Get_NormelizedWeatherDataset
from GadFinalProjectDemo.Models.DataQuery     import MergeUFO_and_Weather_datasets
from GadFinalProjectDemo.Models.DataQuery     import MakeDF_ReadyFor_Analysis


#### Subclasses spawn
db_Functions = create_LocalDatabaseServiceRoutines() 


# Landing page - Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

# Contact page
@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Gad Lidror',
        year=datetime.now().year,
        message='Teacher, Tichonet'
    )

# About Page
@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='Demo for 10th grade internal CS project, Data Science',
        message='This project demonstrate analyzis of imagynary UFO testemonials',
        year=datetime.now().year
     
    )



# -------------------------------------------------------
# Register new user page
# -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            flash('Welcom - '+ form.FirstName.data + " " + form.LastName.data )
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        )


# Data model description, used by the site
@app.route('/DataModel')
def DataModel():
    return render_template(
        'DataModel.html',
        title='This is my Data Model page abou UFO',
        year=datetime.now().year,
        message='In this page we will display the datasets we are going to use in order to answer ARE THERE UFOs'
    )


@app.route('/DataSet1')
def DataSet1():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\UFOTestemonials.csv'))
    raw_data_table = df.sample(30).to_html(classes = 'table table-hover')

    return render_template(
        'DataSet1.html',
        title='UFO testmonials, by place and date',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='This page displays data that can be analyzed and help us understand - ARE THERE UFOs ??'
    )


@app.route('/DataSet2')
def DataSet2():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\weather_description.csv'))
    raw_data_table = df.sample(30).to_html(classes = 'table table-hover')

    return render_template(
        'DataSet2.html',
        title='Weather indications around the world',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='This data set has a description of the weather around the world and enable me to check uf there is a connection between the UFOs apearence and the weather'
    )

@app.route('/DataSet3')
def DataSet3():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\USStatesCodes.csv'))
    raw_data_table = df.sample(30).to_html(classes = 'table table-hover')

    return render_template(
        'DataSet3.html',
        title='State names in the USA',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='This data set enable me to replace short names of states to full names of states'
    )



@app.route('/DataQuery', methods=['GET', 'POST'])
def DataQuery():

    df_ufo = Get_NormelizedUFOTestmonials()

    UFO_table = ""
    fig_image = ""

    form = DataQueryFormStructure(request.form)
    
    #set default values of datetime, to indicate ALL the rows
    minmax = df_ufo['Event_Time']
    form.start_date.data = minmax.min()
    form.end_date.data   = minmax.max()

    #Set the list of states from the data set of all US states
    form.states.choices = get_states_choices() 
   

     
    if (request.method == 'POST' ):

        ##df_ufo = Get_NormelizedUFOTestmonials()
        df_ufo = df_ufo.set_index('State')

        # Get the user's parameters for the query
        states = form.states.data
        start_date = form.start_date.data
        end_date = form.end_date.data
        kind = form.kind.data

        # Get the weather data set
        dff = Get_NormelizedWeatherDataset()

        # Merge the UFO and Weather data sets into onem dataframe
        df_merged = MergeUFO_and_Weather_datasets(dff, df_ufo)

        # no need of this field for the analysis and display

        # Make the merged dataframe ready for anallysis
        df_Merged_analysis = MakeDF_ReadyFor_Analysis(df_merged)
        #df_Merged_analysis = df_Merged_analysis.dropna()

        # Filter only the requested States
        df_ufo_states = df_Merged_analysis.set_index('State').loc[ states ]
        # Filter only the requested Dates
        df_ufo_dates = df_ufo_states.loc[lambda df: (df['Event_Time'] >= start_date) & (df['Event_Time'] <= end_date)]

        # This field was used to set the dates frame requested. The datetime field will show the date
        df_display = df_ufo_states.drop(['Event_Time'], 1)
        UFO_table = df_display.sample(20).to_html()

        # create plot object ready for graphs
        ##fig, ax = plt.subplots()
        fig = plt.figure()
        ax = fig.add_subplot(111)

        #if (kind=='bar'):
        df_graph = df_display.groupby('State').count()
        df_graph = df_graph.nlargest(6, 'datetime') 
        ##plt.figure (figsize=(12,6))
        df_graph['datetime'].plot(ax = ax, kind='barh', grid=True, figsize=(6,3))
        fig_image = plot_to_img(fig)
     


    return render_template('DataQuery.html', 
            form = form, 
            raw_data_table = UFO_table,
            fig_image = fig_image,
            title='User Data Query',
            year=datetime.now().year,
            message='Please enter the parameters you choose, to analyze the database'
        )
