from django.db import models

# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)

class DatabaseManagers(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
        