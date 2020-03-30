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

from GadFinalProjectDemo.Models.DataQuery     import plot_case_1
from GadFinalProjectDemo.Models.DataQuery     import plot_to_img
from GadFinalProjectDemo.Models.DataQuery     import covid19_day_ratio
from GadFinalProjectDemo.Models.DataQuery     import get_countries_choices
from GadFinalProjectDemo.Models.DataQuery     import Get_NormelizedUFOTestmonials
#from GadFinalProjectDemo.Models.general_service_functions import htmlspecialchars

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
    #df_ufo = Get_NormelizedUFOTestmonials()
    #UFO_table = df_ufo.head(20).to_html(classes = 'table table-hover')

    UFO_table = ""

    ##df = df.set_index('Country')

    form = DataQueryFormStructure(request.form)
     
    if (request.method == 'POST' ):
        #name = form.name.data
        Country = ""
        #if (name in df.index):
        #    capital = df.loc[name,'Capital']
        #    raw_data_table = ""
        #else:
        #    capital = name + ', no such country'
        #form.name.data = ''

    return render_template('DataQuery.html', 
            form = form, 
            raw_data_table = UFO_table,
            title='User Data Query',
            year=datetime.now().year,
            message='Please enter the parameters you choose, to analyze the database'
        )
