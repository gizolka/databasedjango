# Generated by Django 2.1.5 on 2019-02-18 14:59

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0029_auto_20190218_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
