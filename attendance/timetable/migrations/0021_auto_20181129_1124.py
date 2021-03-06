# Generated by Django 2.1.3 on 2018-11-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0020_auto_20181122_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(help_text='dd/mm/yy', verbose_name='event date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(help_text='dd/mm/yy', verbose_name='event enddate'),
        ),
    ]
