# Generated by Django 4.2.5 on 2023-12-22 19:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0014_rename_usercource_usercourse'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserCourse',
            new_name='UserCource',
        ),
    ]
