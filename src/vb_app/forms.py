# forms.py
from django import forms

class PlayerForm(forms.Form): #TODO : Ensure that every player has been inserted with at least one position and one team to the database
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(input_formats=['%d.%m.%Y'])
    height = forms.FloatField()
    weight = forms.FloatField()
    position= forms.CharField(max_length=100) 

class CoachForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)

class JuryForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)
