# Generated by Django 4.0.6 on 2022-12-08 07:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muruga', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_credentials',
            new_name='User_credential',
        ),
    ]
