# Generated by Django 2.1 on 2018-11-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0015_auto_20181109_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.DecimalField(decimal_places=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='type_of_event',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Training', 'Training'), ('Workshop', 'Workshop'), ('Meeting', 'Meeting')], default='Conference', max_length=15),
        ),
    ]
