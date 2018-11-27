# Generated by Django 2.1 on 2018-11-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0014_auto_20181109_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(help_text='dd/mm/yy', verbose_name='event date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(help_text='dd/mm/yy', verbose_name='event enddate'),
        ),
        migrations.AlterField(
            model_name='event',
            name='type_of_event',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Training', 'Training'), ('Workshop', 'Workshop'), ('Meeting', 'Meeting')], default='Conference', max_length=2),
        ),
    ]