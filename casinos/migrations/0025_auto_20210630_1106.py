# Generated by Django 3.1.1 on 2021-06-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0024_auto_20210630_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonus',
            name='deposit_number',
        ),
        migrations.AddField(
            model_name='bonus',
            name='bonus_type',
            field=models.CharField(default='No Deposit Bonus', max_length=255, verbose_name='Type bonus'),
        ),
        migrations.AddField(
            model_name='bonus',
            name='is_deposit',
            field=models.CharField(choices=[('0', 'No Deposit'), ('1', 'Deposit')], default=0, max_length=50, verbose_name='Deposit bonus'),
        ),
    ]