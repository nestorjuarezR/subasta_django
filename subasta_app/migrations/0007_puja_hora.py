# Generated by Django 4.0.4 on 2022-07-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subasta_app', '0006_puja'),
    ]

    operations = [
        migrations.AddField(
            model_name='puja',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
    ]
