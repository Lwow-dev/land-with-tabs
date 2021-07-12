# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Casino, Payment, Software, Currency, Countries, Game, Bonus, Appraisal
from .translation import Casino, CasinoTranslationOptions
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

class CasinoAdmin(TabbedTranslationAdmin):  
    list_display = ('name', 'slug', 'is_active', 'position',)
    filter_horizontal = ('pay_en', 'pay_pl', 'pay_de', 'pay_cs', 'pay_sk', 'pay_it', 'pay_hu', 'pay_ro', 'pay_sv', 'pay_nl', 'pay_au', 'pay_ca', 'pay_us', 'pay_gb', 'pay_br', 'pay_fi', 'pay_nz', 'pay_no', 'pay_da', 'pay_es', 'pay_at', 'pay_be', 'pay_bg', 'pay_ch', 'pay_id', 'pay_fr', 'pay_ie', 'pay_in', 'pay_jp', 'pay_my', 'pay_ph', 'pay_sg', 'pay_th', 'pay_tr', 'pay_za', 'providers', 'games', 'country', 'appraisal', 'bonus', 'languages_website', 'languages_support', 'languages_chat')
    search_fields = ('name',)
    ordering = ('position',)
    prepopulated_fields = {"slug": ("name",)}

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'deposit_limit_max', 'deposit_limit_min', 'withdrawal_limit_max', 'withdrawal_limit_min', 'withdrawal_time_max', 'withdrawal_time_min',)
    
class CountriesAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'slug', 'header', 'text')

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class GameAdmin(TabbedTranslationAdmin):
    list_display = ('name_en',)
    
class BonusAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_deposit', 'bonus_type', 'wagering', 'min_dep', 'max_cashout', 'max_bet', 'get_bonus',)

class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('text_appraisal', 'grad_appraisal')
    
admin.site.register(Casino, CasinoAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Appraisal, AppraisalAdmin)