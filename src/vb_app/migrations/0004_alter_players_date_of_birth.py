# Generated by Django 5.0.4 on 2024-05-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vb_app', '0003_remove_coaches_user_remove_juries_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='date_of_birth',
            field=models.TextField(),
        ),
    ]
