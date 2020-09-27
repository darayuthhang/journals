# Generated by Django 3.1.1 on 2020-09-26 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='calendar',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='created_date',
        ),
        migrations.AddField(
            model_name='journal',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
