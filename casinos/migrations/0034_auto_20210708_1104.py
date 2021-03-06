# Generated by Django 3.1.1 on 2021-07-08 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0033_auto_20210708_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paycountry',
            options={'verbose_name': 'Country Pay', 'verbose_name_plural': 'Country Pays'},
        ),
        migrations.RemoveField(
            model_name='casino',
            name='casinoPayCountry',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='deposit_limit_max',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='deposit_limit_min',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='withdrawal_limit_max',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='withdrawal_limit_min',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='withdrawal_time_max',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='withdrawal_time_min',
        ),
        migrations.CreateModel(
            name='CasinoCountryPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_limit_min', models.IntegerField(blank=True, null=True, verbose_name='Deposit limits min')),
                ('deposit_limit_max', models.IntegerField(blank=True, null=True, verbose_name='Deposit limits max')),
                ('withdrawal_limit_min', models.IntegerField(blank=True, null=True, verbose_name='Withdrawal limits min')),
                ('withdrawal_limit_max', models.IntegerField(blank=True, null=True, verbose_name='Withdrawal limits max')),
                ('withdrawal_time_min', models.IntegerField(blank=True, null=True, verbose_name='Withdrawal time min')),
                ('withdrawal_time_max', models.IntegerField(blank=True, null=True, verbose_name='Withdrawal time max')),
                ('casino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casinos.casino')),
                ('countryPay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casinos.paycountry')),
            ],
            options={
                'verbose_name': 'Casino Country Pay',
                'verbose_name_plural': 'Casino Country Pays',
            },
        ),
        migrations.AddField(
            model_name='casino',
            name='casinoCountryPay',
            field=models.ManyToManyField(related_name='casino', through='casinos.CasinoCountryPay', to='casinos.PayCountry'),
        ),
    ]
