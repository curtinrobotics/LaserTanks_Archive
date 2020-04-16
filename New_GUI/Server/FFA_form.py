from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import Required
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class MultiCheckboxField(SelectMultipleField):
	widget			= ListWidget(prefix_label=False)
	option_widget	= CheckboxInput()

class FFAF(Form):
   ''' 
  name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   P1 = TextField("Name Of Player 1",[validators.Required("Please enter your name.")])

   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   
   project = RadioField('Project', choices = [('LT', 'Laser Tank'), 
      ('CC', 'Climbing Clock')])

   language = MultiCheckboxField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python'),('c89', 'C89'),('c99', 'C99')])
   '''
   Nom_player = SelectField(label ='Number of Players', choices=[('1','One Player'),('2','Two Players')
                     ,('3','Three Players'),('4','Four Players')])
   P1 = TextField("Name Of Player 1")
   P2 = TextField("Name Of Player 2")
   P3 = TextField("Name Of Player 3")
   P4 = TextField("Name Of Player 4")
   submit = SubmitField("Send")