# Generated by Django 5.0.4 on 2024-05-11 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vb_app', '0009_rename_team_id_playsin_team_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerinmatch',
            old_name='player',
            new_name='player_username',
        ),
        migrations.AlterUniqueTogether(
            name='playerinmatch',
            unique_together={('session', 'player_username')},
        ),
    ]
