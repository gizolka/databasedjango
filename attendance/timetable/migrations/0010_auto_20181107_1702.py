# Generated by Django 2.1 on 2018-11-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0009_auto_20181107_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(help_text='Format YYYY-MM-DD', verbose_name='event date'),
        ),
    ]
