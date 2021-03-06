# Generated by Django 2.1 on 2018-11-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0011_auto_20181107_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('Speaker', 'Speaker'), ('Attendee', 'Attendee')], default='Speaker', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='type_of_event',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Training', 'Training'), ('Workshop', 'Workshop'), ('Meeting', 'Meeting')], default='Conference', max_length=50),
        ),
    ]
