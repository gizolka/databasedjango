# Generated by Django 2.1.3 on 2019-01-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0026_event_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='department',
            field=models.CharField(choices=[('C3', 'C3'), ('CIRCL', 'CIRCL'), ('CASES', 'CASES')], default='default', max_length=50),
        ),
    ]
