# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Players(models.Model):
    player_username = models.CharField(max_length=50, primary_key=True)
    date_of_birth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='player')

class Coaches(models.Model):
    coach_username = models.CharField(max_length=50, primary_key=True)
    nationality = models.CharField(max_length=50)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='coach')

class Juries(models.Model):
    jury_username = models.CharField(max_length=50, primary_key=True)
    nationality = models.CharField(max_length=50)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='jury')

class Position(models.Model):
    position_id = models.IntegerField(primary_key=True)
    position_name = models.CharField(max_length=50)

class PlayerPositions(models.Model):
    player_positions_ID = models.CharField(max_length=50)  # You might need to adjust this field according to your requirements
    player_username = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('player_username', 'position')  # Define a composite unique constraint

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
    player_username = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_type = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ('player_username', 'team')  # Define a composite unique constraint

class MatchSession(models.Model):
    session_id = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    assigned_jury_username = models.CharField(max_length=50)  # Assuming this field exists in your database schema
    stadium_id = models.IntegerField()  # Assuming this field exists in your database schema
    time_slot = models.DateTimeField()  # Assuming this field exists in your database schema
    date = models.DateField()  # Assuming this field exists in your database schema

    class Meta:
        unique_together = ('stadium_id', 'time_slot', 'date')  # Define a composite unique constraint

class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    stadium_name = models.CharField(max_length=100)
    stadium_country = models.CharField(max_length=50)

class PlayedIn(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    session = models.ForeignKey(MatchSession, on_delete=models.CASCADE)
    time_slot = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ('stadium', 'session', 'time_slot', 'date')  # Define a composite unique constraint

class AssignedTo(models.Model):
    session = models.OneToOneField(MatchSession, primary_key=True, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    assigned_jury_username = models.CharField(max_length=50)
    rating = models.IntegerField(null=True)

class PlayerInMatch(models.Model):
    session = models.ForeignKey(MatchSession, on_delete=models.CASCADE)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('session', 'player')  # Define a composite unique constraint

class PlayedBy(models.Model):
    session = models.OneToOneField(MatchSession, primary_key=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.IntegerField()

    class Meta:
        unique_together = ('team', 'date', 'time_slot')  # Define a composite unique constraint




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


