# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

CURRENCY = (
    ('€', '€'),
    ('$', '$'),
)

LICENSES = (
    ('1', 'Curacao'),
    ('2', 'Malta'),
)

DEPOSIT_BONUS_CHOICES = [
    ('0', 'No Deposit'), 
    ('1', 'Deposit'), 
]

APPRAISAL_CHOICES = [
    ('neg', 'Negatives'),
    ('pos', 'Positives'),
    ('int', 'Interesting Facts')
]

COLORS = (
    ('blue_bg.jpg', 'Blue'),
    ('purple_bg.jpg', 'Purple'),
    ('red_bg.jpg', 'Red'),
    ('green_bg.jpg', 'Green'),
    ('yellow_bg.jpg', 'Yellow'),
    ('azure_bg.jpg', 'Azure'),
    ('orange_bg.jpg', 'Orange'),
)

class Payment(models.Model):
    name =  models.CharField(u'name', max_length=50, blank=False)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/pay/", blank=False, null=False)
    deposit_limit_min = models.IntegerField(u'Deposit limits min', null=True, blank=True)
    deposit_limit_max = models.IntegerField(u'Deposit limits max', null=True, blank=True)
    withdrawal_limit_min = models.IntegerField(u'Withdrawal limits min', null=True, blank=True)
    withdrawal_limit_max = models.IntegerField(u'Withdrawal limits max', null=True, blank=True)
    withdrawal_time_min = models.IntegerField(u'Withdrawal time min', null=True, blank=True)
    withdrawal_time_max = models.IntegerField(u'Withdrawal time max', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Payment"
        verbose_name_plural  = u"Payments"
        
class Countries(models.Model):
    name =  models.CharField(u'Название', max_length=50)
    image = ThumbnailerImageField(u'Flag', upload_to="upload/img/flags/", blank=False)
    currency = models.CharField(u'Currency', max_length=10, choices = CURRENCY, blank=False, default="$")
    slug =  models.CharField(u'Обозначение (en)', max_length=2)
    header = models.CharField(u'Заголовок', max_length=100)
    text = models.CharField(u'Текст', max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Country"
        verbose_name_plural  = u"Countries"
        
class Software(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/soft/", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Software"
        verbose_name_plural  = u"Softwares"
        
class Currency(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/currency/", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Currency"
        verbose_name_plural  = u"Currency"
        
class Game(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/games/", blank=True)
    svg_name = models.CharField(u'svg name in sprite', max_length=50, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Game"
        verbose_name_plural  = u"Games"

class Bonus(models.Model):
    name = models.CharField(u'Title', max_length=255)
    is_deposit = models.CharField(u'Deposit bonus', max_length=50, null=False, blank=False, choices=DEPOSIT_BONUS_CHOICES, default=0)
    bonus_type = models.CharField(u'Type bonus', max_length=255, null=False, blank=False, default='No Deposit Bonus')
    wagering = models.IntegerField(u'Wagering', null=True, blank=True)
    min_dep = models.FloatField(u'Min deposit', null=True, blank=True)
    max_cashout = models.FloatField(u'Max cashout', null=True, blank=True)
    max_bet = models.FloatField(u'Max bet', null=True, blank=True)
    get_bonus = models.CharField(u'Get bonus', max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Bonus"
        verbose_name_plural  = u"Bonuses"

class Appraisal(models.Model):
    text_appraisal = models.CharField(u'Text', max_length=255, blank=False, null=False)
    grad_appraisal = models.CharField(u'Gradation', max_length=50, choices=APPRAISAL_CHOICES, null=False, blank=False, default='pos')

    def __str__(self):
        return self.text_appraisal
    
    class Meta:
        verbose_name  = u"Appraisal"
        verbose_name_plural  = u"Appraisals"

class Casino(models.Model):

    is_active = models.BooleanField(u'Is Active', default=False, blank=False, null=False)
    name =  models.CharField(u'Title', max_length=50)
    slug = models.SlugField(u'URL',blank=True, null=True)
    color = models.CharField(u'Color Background', max_length=50, choices = COLORS)
    link = models.CharField(u'Link', max_length=180, blank=False, null=True, default="#")
    reg_link = models.CharField(u'Reg Link', max_length=180, blank=True, null=True)
    bonus_link = models.CharField(u'Bonus Link', max_length=180, blank=True, null=True)
    details_text_visible = models.TextField(u'Details text visible', null=True, blank=True)
    details_text_hidden = models.TextField(u'Details text hidden', null=True, blank=True)
    bonuses_text = models.TextField(u'Bonuses text', null=True, blank=True)
    reputation_text = models.TextField(u'Reputation text', null=True, blank=True)
    pay_text = models.TextField(u'Payment text', null=True, blank=True)
    revenues_score = models.IntegerField(u'Revenues Score', default=100, blank=False, null=False)
    terms_score = models.IntegerField(u'Terms Score', default=100, blank=False, null=False)
    blacklist_score = models.IntegerField(u'Blacklist Score', default=100, blank=False, null=False)
    complaints_score = models.IntegerField(u'Complaints Score', default=100, blank=False, null=False)
    other_score = models.IntegerField(u'Other factors Score', default=100, blank=False, null=False)
    license = models.CharField(u'License', max_length=3, choices = LICENSES, default=2)
    logo = ThumbnailerImageField(u'Casino Logo', upload_to="upload/img/logos/")
    baner = ThumbnailerImageField(u'Casino Baner', upload_to="upload/img/promo/", blank=False, null=True)
    screen = ThumbnailerImageField(u'Screen Shot', upload_to="upload/img/screens/", blank=False, null=True)
    position = models.IntegerField(u'Position EN', default=0, blank=False, null=False)
    adv1 = models.CharField(u'Promo1 EN', max_length=50, blank=True, null=True)
    adv2 = models.CharField(u'Promo2 EN', max_length=50, blank=True, null=True)
    adv3 = models.CharField(u'Promo3 EN', max_length=50, blank=True, null=True)
    adv4 = models.CharField(u'Promo4 EN', max_length=50, blank=True, null=True)
    promocode = models.CharField(u'Promo Code', max_length=20, blank=True, null=True)
    min_dep = models.IntegerField(u'Min deposit', blank=False, null=False, default=0)
    limit = models.IntegerField(u'Bonus limit', null=False, blank=False, default=0)
    fs = models.IntegerField(u'Free Spins', null=False, blank=False, default=0)
    
    bonus = models.ManyToManyField(Bonus, related_name='bonuses', blank=True)
    providers = models.ManyToManyField(Software, related_name='providers', blank=True)
    games = models.ManyToManyField(Game, related_name='games', blank=True)
    country = models.ManyToManyField(Countries, related_name='countries', blank=True)
    appraisal =  models.ManyToManyField(Appraisal, related_name='Appraisal', blank=True)
    languages_website = models.ManyToManyField(Countries, related_name='languages_website', blank=True)
    languages_support = models.ManyToManyField(Countries, related_name='languages_support', blank=True)
    languages_chat = models.ManyToManyField(Countries, related_name='languages_chat', blank=True)
    pay_en = models.ManyToManyField(Payment, related_name='pays_en', blank=True)
    pay_pl = models.ManyToManyField(Payment, related_name='pays_pl', blank=True)
    pay_de = models.ManyToManyField(Payment, related_name='pays_de', blank=True)
    pay_cs = models.ManyToManyField(Payment, related_name='pays_cs', blank=True)
    pay_sk = models.ManyToManyField(Payment, related_name='pays_sk', blank=True)
    pay_it = models.ManyToManyField(Payment, related_name='pays_it', blank=True)
    pay_hu = models.ManyToManyField(Payment, related_name='pays_hu', blank=True)
    pay_ro = models.ManyToManyField(Payment, related_name='pays_ro', blank=True)
    pay_sv = models.ManyToManyField(Payment, related_name='pays_sv', blank=True)
    pay_nl = models.ManyToManyField(Payment, related_name='pays_nl', blank=True)
    pay_au = models.ManyToManyField(Payment, related_name='pays_au', blank=True)
    pay_ca = models.ManyToManyField(Payment, related_name='pays_ca', blank=True)
    pay_us = models.ManyToManyField(Payment, related_name='pays_us', blank=True)
    pay_gb = models.ManyToManyField(Payment, related_name='pays_gb', blank=True)
    pay_br = models.ManyToManyField(Payment, related_name='pays_br', blank=True)
    pay_fi = models.ManyToManyField(Payment, related_name='pays_fi', blank=True)
    pay_nz = models.ManyToManyField(Payment, related_name='pays_nz', blank=True)
    pay_no = models.ManyToManyField(Payment, related_name='pays_no', blank=True)
    pay_da = models.ManyToManyField(Payment, related_name='pays_da', blank=True)
    pay_at = models.ManyToManyField(Payment, related_name='pays_at', blank=True)
    pay_be = models.ManyToManyField(Payment, related_name='pays_be', blank=True)
    pay_bg = models.ManyToManyField(Payment, related_name='pays_bg', blank=True)
    pay_ch = models.ManyToManyField(Payment, related_name='pays_ch', blank=True)
    pay_es = models.ManyToManyField(Payment, related_name='pays_es', blank=True)
    pay_fr = models.ManyToManyField(Payment, related_name='pays_fr', blank=True)
    pay_id = models.ManyToManyField(Payment, related_name='pays_id', blank=True)
    pay_ie = models.ManyToManyField(Payment, related_name='pays_ie', blank=True)
    pay_in = models.ManyToManyField(Payment, related_name='pays_in', blank=True)
    pay_jp = models.ManyToManyField(Payment, related_name='pays_jp', blank=True)
    pay_my = models.ManyToManyField(Payment, related_name='pays_my', blank=True)
    pay_ph = models.ManyToManyField(Payment, related_name='pays_ph', blank=True)
    pay_sg = models.ManyToManyField(Payment, related_name='pays_sg', blank=True)
    pay_th = models.ManyToManyField(Payment, related_name='pays_th', blank=True)
    pay_za = models.ManyToManyField(Payment, related_name='pays_za', blank=True)
    pay_tr = models.ManyToManyField(Payment, related_name='pays_tr', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name  = u"Casino"
        verbose_name_plural  = u"Casinos"