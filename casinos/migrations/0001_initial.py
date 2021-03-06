# Generated by Django 3.1.1 on 2021-05-24 11:18

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='upload/img/flags/', verbose_name='Flag')),
                ('currency', models.CharField(choices=[('€', '€'), ('$', '$')], default='$', max_length=10, verbose_name='Currency')),
                ('slug', models.CharField(max_length=2, verbose_name='Обозначение (en)')),
                ('header', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=300, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('logo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='upload/img/currency/', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currency',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('logo', easy_thumbnails.fields.ThumbnailerImageField(upload_to='upload/img/pay/', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('logo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='upload/img/soft/', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Software',
                'verbose_name_plural': 'Softwares',
            },
        ),
        migrations.CreateModel(
            name='Casino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('name', models.CharField(max_length=50, verbose_name='Title')),
                ('color', models.CharField(default='#000000', help_text='Пример - #fff000', max_length=10, verbose_name='Color RGB')),
                ('trust_score', models.CharField(choices=[('50', '5.0'), ('49', '4.9'), ('48', '4.8'), ('47', '4.7'), ('46', '4.6'), ('45', '4.5'), ('44', '4.4'), ('43', '4.3'), ('42', '4.2'), ('41', '4.1'), ('40', '4.0'), ('35', '3.5'), ('30', '3.0'), ('25', '2.5'), ('20', '2.0'), ('15', '1.5'), ('10', '1.0'), ('0', '0.0')], max_length=3, verbose_name='Trust & Fairness Score')),
                ('license', models.CharField(choices=[('1', 'Curacao'), ('2', 'Malta')], default=2, max_length=3, verbose_name='License')),
                ('logo', easy_thumbnails.fields.ThumbnailerImageField(upload_to='upload/img/logos/', verbose_name='Casino Logo')),
                ('position_en', models.IntegerField(default=0, verbose_name='Position EN')),
                ('link_en', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link EN')),
                ('adv1_en', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 EN')),
                ('adv2_en', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 EN')),
                ('adv3_en', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 EN')),
                ('position_pl', models.IntegerField(default=0, verbose_name='Position PL')),
                ('link_pl', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_pl', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 PL')),
                ('adv2_pl', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 PL')),
                ('adv3_pl', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 PL')),
                ('position_de', models.IntegerField(default=0, verbose_name='Position DE')),
                ('link_de', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_de', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 DE')),
                ('adv2_de', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 DE')),
                ('adv3_de', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 DE')),
                ('position_cs', models.IntegerField(default=0, verbose_name='Position CS')),
                ('link_cs', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_cs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 CS')),
                ('adv2_cs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 CS')),
                ('adv3_cs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 CS')),
                ('position_sk', models.IntegerField(default=0, verbose_name='Position SK')),
                ('link_sk', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_sk', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 SK')),
                ('adv2_sk', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 SK')),
                ('adv3_sk', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 SK')),
                ('position_it', models.IntegerField(default=0, verbose_name='Position IT')),
                ('link_it', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_it', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 IT')),
                ('adv2_it', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 IT')),
                ('adv3_it', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 IT')),
                ('position_hu', models.IntegerField(default=0, verbose_name='Position HU')),
                ('link_hu', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_hu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 HU')),
                ('adv2_hu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 HU')),
                ('adv3_hu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 HU')),
                ('position_ro', models.IntegerField(default=0, verbose_name='Position RO')),
                ('link_ro', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_ro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 RO')),
                ('adv2_ro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 RO')),
                ('adv3_ro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 RO')),
                ('position_sv', models.IntegerField(default=0, verbose_name='Position SV')),
                ('link_sv', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_sv', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 SV')),
                ('adv2_sv', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 SV')),
                ('adv3_sv', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 SV')),
                ('position_nl', models.IntegerField(default=0, verbose_name='Position NL')),
                ('link_nl', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_nl', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 NL')),
                ('adv2_nl', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 NL')),
                ('adv3_nl', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 NL')),
                ('position_au', models.IntegerField(default=0, verbose_name='Position AU')),
                ('link_au', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_au', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 AU')),
                ('adv2_au', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 AU')),
                ('adv3_au', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 AU')),
                ('position_ca', models.IntegerField(default=0, verbose_name='Position CA')),
                ('link_ca', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_ca', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 CA')),
                ('adv2_ca', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 CA')),
                ('adv3_ca', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 CA')),
                ('position_us', models.IntegerField(default=0, verbose_name='Position US')),
                ('link_us', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_us', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 US')),
                ('adv2_us', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 US')),
                ('adv3_us', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 US')),
                ('position_gb', models.IntegerField(default=0, verbose_name='Position GB')),
                ('link_gb', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_gb', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 GB')),
                ('adv2_gb', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 GB')),
                ('adv3_gb', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 GB')),
                ('position_br', models.IntegerField(default=0, verbose_name='Position BR')),
                ('link_br', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_br', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 BR')),
                ('adv2_br', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 BR')),
                ('adv3_br', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 BR')),
                ('position_fi', models.IntegerField(default=0, verbose_name='Position FI')),
                ('link_fi', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_fi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 FI')),
                ('adv2_fi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 FI')),
                ('adv3_fi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 FI')),
                ('position_nz', models.IntegerField(default=0, verbose_name='Position NZ')),
                ('link_nz', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_nz', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 NZ')),
                ('adv2_nz', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 NZ')),
                ('adv3_nz', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 NZ')),
                ('position_no', models.IntegerField(default=0, verbose_name='Position NO')),
                ('link_no', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 NO')),
                ('adv2_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 NO')),
                ('adv3_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 NO')),
                ('position_da', models.IntegerField(default=0, verbose_name='Position DA')),
                ('link_da', models.CharField(blank=True, help_text='Если в ссылке уже есть знак ? то она должна оканчиваться на знак &, если нет, то на знак ?', max_length=180, null=True, verbose_name='Link')),
                ('adv1_da', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo1 DA')),
                ('adv2_da', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo2 DA')),
                ('adv3_da', models.CharField(blank=True, max_length=50, null=True, verbose_name='Promo3 DA')),
                ('min_dep', models.IntegerField(default=0, verbose_name='Min deposit')),
                ('bonus', models.IntegerField(default=0, verbose_name='Welcome bonus')),
                ('limit', models.IntegerField(default=0, verbose_name='Bonus limit')),
                ('fs', models.IntegerField(default=0, verbose_name='Free Spins')),
                ('country', models.ManyToManyField(blank=True, related_name='countries', to='casinos.Countries')),
                ('pay_au', models.ManyToManyField(blank=True, related_name='pays_au', to='casinos.Payment')),
                ('pay_br', models.ManyToManyField(blank=True, related_name='pays_br', to='casinos.Payment')),
                ('pay_ca', models.ManyToManyField(blank=True, related_name='pays_ca', to='casinos.Payment')),
                ('pay_cs', models.ManyToManyField(blank=True, related_name='pays_cs', to='casinos.Payment')),
                ('pay_da', models.ManyToManyField(blank=True, related_name='pays_da', to='casinos.Payment')),
                ('pay_de', models.ManyToManyField(blank=True, related_name='pays_de', to='casinos.Payment')),
                ('pay_en', models.ManyToManyField(blank=True, related_name='pays_en', to='casinos.Payment')),
                ('pay_fi', models.ManyToManyField(blank=True, related_name='pays_fi', to='casinos.Payment')),
                ('pay_gb', models.ManyToManyField(blank=True, related_name='pays_gb', to='casinos.Payment')),
                ('pay_hu', models.ManyToManyField(blank=True, related_name='pays_hu', to='casinos.Payment')),
                ('pay_it', models.ManyToManyField(blank=True, related_name='pays_it', to='casinos.Payment')),
                ('pay_nl', models.ManyToManyField(blank=True, related_name='pays_nl', to='casinos.Payment')),
                ('pay_no', models.ManyToManyField(blank=True, related_name='pays_no', to='casinos.Payment')),
                ('pay_nz', models.ManyToManyField(blank=True, related_name='pays_nz', to='casinos.Payment')),
                ('pay_pl', models.ManyToManyField(blank=True, related_name='pays_pl', to='casinos.Payment')),
                ('pay_ro', models.ManyToManyField(blank=True, related_name='pays_ro', to='casinos.Payment')),
                ('pay_sk', models.ManyToManyField(blank=True, related_name='pays_sk', to='casinos.Payment')),
                ('pay_sv', models.ManyToManyField(blank=True, related_name='pays_sv', to='casinos.Payment')),
                ('pay_us', models.ManyToManyField(blank=True, related_name='pays_us', to='casinos.Payment')),
            ],
            options={
                'verbose_name': 'Casino',
                'verbose_name_plural': 'Casinos',
            },
        ),
    ]
