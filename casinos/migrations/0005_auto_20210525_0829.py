# Generated by Django 3.1.1 on 2021-05-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0004_casino_providers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='providers',
            field=models.ManyToManyField(blank=True, related_name='providers', to='casinos.Software'),
        ),
    ]
