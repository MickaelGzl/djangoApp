# Generated by Django 5.0 on 2023-12-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cours_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='numberOfNote',
            field=models.IntegerField(default=0),
        ),
    ]
