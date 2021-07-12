# Generated by Django 3.1.1 on 2021-06-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0023_auto_20210609_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_appraisal', models.CharField(max_length=255, verbose_name='Text')),
                ('grad_appraisal', models.CharField(choices=[('neg', 'Negatives'), ('pos', 'Positives'), ('int', 'Interesting Facts')], default='pos', max_length=50, verbose_name='Gradation')),
            ],
            options={
                'verbose_name': 'Appraisal',
                'verbose_name_plural': 'Appraisals',
            },
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
                ('deposit_number', models.CharField(choices=[('0', 'No Deposit'), ('1', '1st Deposit'), ('2', '2nd Deposit'), ('3', '3rd Deposit')], default=0, max_length=50, verbose_name='Deposit bonus')),
                ('wagering', models.IntegerField(blank=True, null=True, verbose_name='Wagering')),
                ('min_dep', models.IntegerField(blank=True, null=True, verbose_name='Min deposit')),
                ('max_cashout', models.IntegerField(blank=True, null=True, verbose_name='Max cashout')),
                ('max_bet', models.IntegerField(blank=True, null=True, verbose_name='Max bet')),
                ('get_bonus', models.CharField(max_length=50, verbose_name='Get bonus')),
            ],
            options={
                'verbose_name': 'Bonus',
                'verbose_name_plural': 'Bonuses',
            },
        ),
        migrations.RemoveField(
            model_name='casino',
            name='bonus_score',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='games_score',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='payout_score',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='trust_score',
        ),
        migrations.AddField(
            model_name='casino',
            name='blacklist_score',
            field=models.IntegerField(default=100, verbose_name='Blacklist Score'),
        ),
        migrations.AddField(
            model_name='casino',
            name='bonuses_text',
            field=models.TextField(blank=True, null=True, verbose_name='Bonuses text'),
        ),
        migrations.AddField(
            model_name='casino',
            name='complaints_score',
            field=models.IntegerField(default=100, verbose_name='Complaints Score'),
        ),
        migrations.AddField(
            model_name='casino',
            name='details_text',
            field=models.TextField(blank=True, null=True, verbose_name='Details text'),
        ),
        migrations.AddField(
            model_name='casino',
            name='languages_chat',
            field=models.ManyToManyField(blank=True, related_name='languages_chat', to='casinos.Countries'),
        ),
        migrations.AddField(
            model_name='casino',
            name='languages_support',
            field=models.ManyToManyField(blank=True, related_name='languages_support', to='casinos.Countries'),
        ),
        migrations.AddField(
            model_name='casino',
            name='languages_website',
            field=models.ManyToManyField(blank=True, related_name='languages_website', to='casinos.Countries'),
        ),
        migrations.AddField(
            model_name='casino',
            name='other_score',
            field=models.IntegerField(default=100, verbose_name='Other factors Score'),
        ),
        migrations.AddField(
            model_name='casino',
            name='pay_text',
            field=models.TextField(blank=True, null=True, verbose_name='Payment text'),
        ),
        migrations.AddField(
            model_name='casino',
            name='reputation_text',
            field=models.TextField(blank=True, null=True, verbose_name='Reputation text'),
        ),
        migrations.AddField(
            model_name='casino',
            name='revenues_score',
            field=models.IntegerField(default=100, verbose_name='Revenues Score'),
        ),
        migrations.AddField(
            model_name='casino',
            name='terms_score',
            field=models.IntegerField(default=100, verbose_name='Terms Score'),
        ),
        migrations.AddField(
            model_name='payment',
            name='deposit_limit_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Deposit limits max'),
        ),
        migrations.AddField(
            model_name='payment',
            name='deposit_limit_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Deposit limits min'),
        ),
        migrations.AddField(
            model_name='payment',
            name='withdrawal_limit_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Withdrawal limits max'),
        ),
        migrations.AddField(
            model_name='payment',
            name='withdrawal_limit_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Withdrawal limits min'),
        ),
        migrations.AddField(
            model_name='payment',
            name='withdrawal_time_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Withdrawal time max'),
        ),
        migrations.AddField(
            model_name='payment',
            name='withdrawal_time_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Withdrawal time min'),
        ),
        migrations.RemoveField(
            model_name='casino',
            name='bonus',
        ),
        migrations.AlterField(
            model_name='casino',
            name='color',
            field=models.CharField(choices=[('blue_bg.jpg', 'Blue'), ('purple_bg.jpg', 'Purple'), ('red_bg.jpg', 'Red'), ('green_bg.jpg', 'Green'), ('yellow_bg.jpg', 'Yellow'), ('azure_bg.jpg', 'Azure'), ('orange_bg.jpg', 'Orange')], max_length=50, verbose_name='Color Background'),
        ),
        migrations.AddField(
            model_name='casino',
            name='appraisal',
            field=models.ManyToManyField(blank=True, related_name='Appraisal', to='casinos.Appraisal'),
        ),
        migrations.AddField(
            model_name='casino',
            name='bonus',
            field=models.ManyToManyField(blank=True, related_name='Bonus', to='casinos.Bonus'),
        ),
    ]
