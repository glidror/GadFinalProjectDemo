"""
Project by: Gad Lidror (Demo)
Date: TASHAP
Grade: 10th grade, Tichonet

This file include all the redirections of the different pages, and thier routs
It has most of the logic of the project, written in Python, under Flask, WTF and more
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import io
import base64
import json 
import requests

from GadFinalProjectDemo import app

from flask   import Flask, render_template, flash, redirect, request
from flask_wtf import FlaskForm

from wtforms import Form, validators, ValidationError
from wtforms import BooleanField, StringField, PasswordField, TextField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

from datetime import datetime
from os import path


#### Subclasses spawn
from GadFinalProjectDemo.Models.QueryFormStructure import QueryFormStructure 


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/Album')
def Album():
    """Renders the about page."""
    return render_template(
        'PictureAlbum.html',
        title='Pictures',
        year=datetime.now().year,
        message='Welcome to my picture album'
    )


@app.route('/Query', methods=['GET', 'POST'])
def Query():

    Name = None
    capital = ''
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\capitals.csv'))
    df = df.set_index('Country')

    form = QueryFormStructure(request.form)
     
    if (request.method == 'POST' ):
        name = form.name.data
        
        if (name in df.index):
            capital = df.loc[name,'Capital']
        else:
            capital = name + ', no such country'
        ###form.name.data = ''

    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('Query.html', 
            form = form, 
            name = capital, 
            raw_data_table = raw_data_table,
            title='Query by the user',
            year=datetime.now().year,
            message='This page will use the web forms to get user input'
        )


