# Generated by Django 2.1 on 2018-11-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0010_auto_20181107_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='event date'),
        ),
    ]
