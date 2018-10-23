# Generated by Django 2.1 on 2018-10-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('', '----'), ('SP', 'Speaker'), ('AT', 'Attendee'), ('TR', 'Trainer')], max_length=50),
        ),
    ]
