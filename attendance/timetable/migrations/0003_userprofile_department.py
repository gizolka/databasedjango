# Generated by Django 2.1 on 2018-09-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20180926_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(default='', max_length=100),
        ),
    ]