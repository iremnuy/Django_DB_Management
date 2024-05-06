# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Coach(models.Model):
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    nationality = models.TextField(blank=True, null=True,unique=True)

    class Meta:
        managed = False
        db_table = 'Coach'


class Dbmanager(models.Model):
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DBManager'


class Jury(models.Model):
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    nationality = models.TextField(blank=True, null=True,unique=True)

    class Meta:
        managed = False
        db_table = 'Jury'


class Matchsession(models.Model):
    session_id = models.BigIntegerField(db_column='session_ID', blank=True, null=True)  # Field name made lowercase.
    team_id = models.BigIntegerField(db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    stadium_id = models.BigIntegerField(db_column='stadium_ID', blank=True, null=True)  # Field name made lowercase.
    stadium_name = models.TextField(blank=True, null=True)
    stadium_country = models.TextField(blank=True, null=True)
    time_slot = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    assigned_jury_username = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MatchSession'


class Player(models.Model):
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    date_of_birth = models.TextField(blank=True, null=True)
    height = models.BigIntegerField(blank=True, null=True)
    weight = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player'


class Playerpositions(models.Model):
    player_positions_id = models.BigIntegerField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlayerPositions'


class Playerteams(models.Model):
    player_teams_id = models.BigIntegerField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    team = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlayerTeams'


class Position(models.Model):
    position_id = models.BigIntegerField(db_column='position_ID', blank=True, null=True)  # Field name made lowercase.
    position_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Position'


class Sessionsquads(models.Model):
    squad_id = models.BigIntegerField(db_column='squad_ID', blank=True, null=True)  # Field name made lowercase.
    session_id = models.BigIntegerField(db_column='session_ID', blank=True, null=True)  # Field name made lowercase.
    played_player_username = models.TextField(blank=True, null=True)
    position_id = models.BigIntegerField(db_column='position_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SessionSquads'


class Team(models.Model):
    team_id = models.BigIntegerField(db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    team_name = models.TextField(blank=True, null=True)
    coach_username = models.TextField(blank=True, null=True)
    contract_start = models.TextField(blank=True, null=True)
    contract_finish = models.TextField(blank=True, null=True)
    channel_id = models.BigIntegerField(db_column='channel_ID', blank=True, null=True)  # Field name made lowercase.
    channel_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Team'


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
