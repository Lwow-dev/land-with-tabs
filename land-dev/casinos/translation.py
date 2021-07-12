# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import Casino, Countries, Game

class CasinoTranslationOptions(TranslationOptions):
    fields = ('link', 'adv1', 'adv2', 'adv3', 'adv4',)
    
class CountriesTranslationOptions(TranslationOptions):
    fields = ('text', 'header',)
    
class GameTranslationOptions(TranslationOptions):
    fields = ('name',)
    
translator.register(Casino, CasinoTranslationOptions)
translator.register(Game, GameTranslationOptions)
translator.register(Countries, CountriesTranslationOptions)