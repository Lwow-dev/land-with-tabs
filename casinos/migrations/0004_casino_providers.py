# Generated by Django 3.1.1 on 2021-05-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0003_casino_baner'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='providers',
            field=models.ManyToManyField(blank=True, related_name='Providers', to='casinos.Software'),
        ),
    ]
