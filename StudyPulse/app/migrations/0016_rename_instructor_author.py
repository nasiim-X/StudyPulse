# Generated by Django 4.2.5 on 2023-12-22 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_usercourse_usercource'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instructor',
            new_name='Author',
        ),
    ]