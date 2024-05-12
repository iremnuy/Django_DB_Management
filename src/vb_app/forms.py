# forms.py
from django import forms

class PlayerForm(forms.Form): #TODO : Ensure that every player has been inserted with at least one position and one team to the database
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'])
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

class MatchForm(forms.Form):
    date = forms.DateField(input_formats=['%Y-%m-%d'])
    time_slot = forms.IntegerField()
    stadium = forms.CharField(max_length=50)
    jury_name= forms.CharField(max_length=50)
    jury_surname= forms.CharField(max_length=50)
    team_id= forms.IntegerField() #only its current team

class SquadForm(forms.Form):
    player1 = forms.CharField()
    player2 = forms.CharField()
    player3 = forms.CharField()
    player4 = forms.CharField()
    player5 = forms.CharField()
    player6 = forms.CharField()
    team_id = forms.IntegerField()
    session_id = forms.IntegerField()
    position1 = forms.IntegerField()
    position2 = forms.IntegerField()
    position3 = forms.IntegerField()
    position4 = forms.IntegerField()
    position5 = forms.IntegerField()
    position6 = forms.IntegerField()
