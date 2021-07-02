# Generated by Django 3.1.1 on 2021-06-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0015_auto_20210607_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='adv1_ie',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 EN'),
        ),
        migrations.AddField(
            model_name='casino',
            name='adv2_ie',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 EN'),
        ),
        migrations.AddField(
            model_name='casino',
            name='adv3_ie',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 EN'),
        ),
        migrations.AddField(
            model_name='casino',
            name='adv4_ie',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo4 EN'),
        ),
        migrations.AddField(
            model_name='casino',
            name='link_ie',
            field=models.CharField(default='#', max_length=180, null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='countries',
            name='header_ie',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='countries',
            name='text_ie',
            field=models.CharField(max_length=300, null=True, verbose_name='Текст'),
        ),
    ]
