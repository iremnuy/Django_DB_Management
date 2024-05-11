# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from volleyball_db import settings


class Players(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length=50,null=True)
    date_of_birth = models.TextField()
    height = models.IntegerField()
    weight = models.IntegerField()

class Coaches(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    nationality = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)

class Juries(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    nationality = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)


class Position(models.Model):
    position_id = models.IntegerField(primary_key=True)
    position_name = models.CharField(max_length=50)

class PlayerPositions(models.Model):
    player_positions_ID = models.CharField(max_length=50, null=True)  # You might need to adjust this field according to your requirements
    username = models.CharField(max_length=50, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('username', 'position')  # Define a composite unique constraint

class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=100)

class Contract(models.Model):
    team = models.OneToOneField(Team, primary_key=True, on_delete=models.CASCADE)
    coach_username = models.CharField(max_length=50)
    contract_start = models.DateField()
    contract_finish = models.DateField()

class Channel(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    channel_name = models.CharField(max_length=100)

class Agreement(models.Model):
    team = models.OneToOneField(Team, primary_key=True, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

class PlaysIn(models.Model):
    username = models.CharField(max_length=50,null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True)
    #player_teams_ID = models.IntegerField(null=True)  # You might need to adjust this field according to your requirements, primary key yap irem
    
    class Meta:
        unique_together = ('username', 'team')  # Define a composite unique constraint

class MatchSession(models.Model):
    session_id = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True) #nulllable ise burayı öyle yap 
    #assigned_jury_username = models.ForeignKey(Juries,max_length=50, null=True,on_delete=models.CASCADE) # Attention maybe it is not cascade
     # Assuming this field exists in your database schema
    #stadium_id = models.IntegerField( null=True)  # Assuming this field exists in your database schema
    #time_slot = models.DateTimeField(null=True )  # Assuming this field exists in your database schema
    #date = models.DateField(null=True)  # Assuming this field exists in your database schema


    class Meta:
        unique_together = ('session_id', 'team')  # Define a composite unique constraint
         #irem : sildim burayo neden var ki , yanlış 

class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    stadium_name = models.CharField(max_length=100)
    stadium_country = models.CharField(max_length=50)

class PlayedIn(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(MatchSession, on_delete=models.CASCADE, null=True, unique=True)
    time_slot = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ('stadium', 'time_slot', 'date')  # Define a composite unique constraint irem değiştirdim 

class AssignedTo(models.Model):
    session = models.OneToOneField(MatchSession, primary_key=True, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, null=True)
    assigned_jury_username = models.CharField(max_length=50)
    rating = models.FloatField(null=True)

class PlayerInMatch(models.Model):
    session = models.ForeignKey(MatchSession, on_delete=models.CASCADE, null=True)
    player_username = models.ForeignKey(Players, on_delete=models.CASCADE, null=True, to_field='username')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('session', 'player_username')  # Define a composite unique constraint

class PlayedBy(models.Model):
    session = models.OneToOneField(MatchSession, primary_key=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    time_slot = models.IntegerField()

    class Meta:
        unique_together = ('team', 'date', 'time_slot')  # Define a composite unique constraint


