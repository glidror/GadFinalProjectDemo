
### ----------------------------------------------------------- ###
### --- include all software packages and libraries needed ---- ###
### ----------------------------------------------------------- ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
from os import path



from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import TextField, TextAreaField, SelectField, SelectMultipleField, DateField, DateTimeField
from wtforms import StringField, PasswordField, HiddenField, SubmitField
from wtforms import IntegerField, DecimalField, FloatField, RadioField, BooleanField

from wtforms import validators
from wtforms import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

from wtforms.fields.html5 import DateField
### ----------------------------------------------------------- ###





## This class have the fields that are part of the Login form.
##   This form will get from the user a 'username' and a 'password' and sent to the server
##   to check if this user is authorised to continue
## You can see three fields:
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class LoginFormStructure(FlaskForm):
    username = StringField('User name:  ' , validators = [DataRequired()])
    password = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit   = SubmitField('Submit')



## This class have the fields of a registration form
##   This form is where the user can register himself. It will have sll the information
##   we want to save on a user (general information) and the username ans PW the new user want to have
## You can see three fields:
##   the 'FirstName' field - will be used to get the first name of the user
##   the 'LastName' field - will be used to get the last name of the user
##   the 'PhoneNum' field - will be used to get the phone number of the user
##   the 'EmailAddr' field - will be used to get the E-Mail of the user
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')


### ----------------------------------------------------------- ###
###      Action Buttons
### ----------------------------------------------------------- ###
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"
### ----------------------------------------------------------- ###
class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"
### ----------------------------------------------------------- ###


## This class have the fields that are part of the data query of the project
## You can see two fields:
##   the 'states' field - enable to choose multiple states for the query
##   the 'start_date' field - begin of date to start search of UFO testemonials
##   the 'end_date' field - end of date to start search of UFO testemonials
##   the 'kind' field - the type of graph that will be displayed
class DataQueryFormStructure(FlaskForm):
    states = SelectMultipleField('Select Multiple:', validators = [DataRequired()] )
    start_date = DateField('Start Date:' , format='%Y-%m-%d' , validators = [DataRequired()])
    end_date   = DateField('End   Date:' , format='%Y-%m-%d' , validators = [DataRequired()])
    kind = SelectField('Chart Kind' , validators = [DataRequired()] , choices=[('line', 'line'), ('bar', 'bar')])
    submit = SubmitField('Submit')


