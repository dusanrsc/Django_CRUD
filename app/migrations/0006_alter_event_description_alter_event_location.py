# Generated by Django 5.0 on 2023-12-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_places_event_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=20),
        ),
    ]