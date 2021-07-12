# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Casino, Payment, Software, Currency, Countries, Game, Bonus, Appraisal, PayCountry, CasinoCountryPay
from .translation import Casino, CasinoTranslationOptions
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

class CasinoAdmin(TabbedTranslationAdmin):  
    list_display = ('name', 'slug', 'is_active', 'position',)
    filter_horizontal = ('providers', 'games', 'country', 'appraisal', 'bonus', 'languages_website', 'languages_support', 'languages_chat')
    search_fields = ('name',)
    ordering = ('position',)
    prepopulated_fields = {"slug": ("name",)}

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name',  )
    search_fields = ('name',)
    
class CountriesAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'slug', 'header', 'text', )
    search_fields = ('name',)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class GameAdmin(TabbedTranslationAdmin):
    list_display = ('name_en',)
    
class BonusAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_deposit', 'bonus_type', 'wagering', 'min_dep', 'max_cashout', 'max_bet', 'get_bonus',)
    search_fields = ('name',)

class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('text_appraisal', 'grad_appraisal')
    
class PayCountryAdmin(admin.ModelAdmin):
    list_display = ('payment', 'countries')

class CasinoCountryPayAdmin(admin.ModelAdmin):
    list_display = ('casino',  'countryPay', 'deposit_limit_min', 'deposit_limit_max', 'withdrawal_limit_min', 'withdrawal_limit_max', 'withdrawal_time_min', 'withdrawal_time_max',)
    search_fields = ('casino',)
    
admin.site.register(Casino, CasinoAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Appraisal, AppraisalAdmin)
admin.site.register(PayCountry, PayCountryAdmin)
admin.site.register(CasinoCountryPay, CasinoCountryPayAdmin)
