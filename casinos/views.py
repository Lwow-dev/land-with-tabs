# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

import random
import os
import numpy as np

from django.utils import translation

from .models import Casino, Software, Countries, Game, PayCountry, CasinoCountryPay
from django.views.decorators.cache import never_cache

def get_anid(request):
    if 'anid' in request.GET:
        gambler_id = request.GET['anid']
    elif 'payload' in request.GET:
        gambler_id = request.GET['payload']
    elif 'clickid' in request.GET:
        gambler_id = request.GET['clickid']
    else:
        gambler_id=0
    return gambler_id

@never_cache
def home(request):
    if request.GET:
        gambler_id = get_anid(request)
        param = 'anid=' + gambler_id
    else:
        gambler_id=False
        param = False
    
    link = 'https://top10kasino.com'
    
    if gambler_id and param:
        fulllink = link + '/?' + param
    else:
        fulllink = link + '/'
    return redirect(fulllink)

@never_cache
def show_review(request, review_slug):
    casino = get_object_or_404(Casino, slug=review_slug)
    games = Game.objects.all()

    if request.GET:
        gambler_id = get_anid(request)
    else:
        gambler_id=False

    bonus_no_deposit = casino.bonus.filter(is_deposit = '0')
    bonus_deposit = casino.bonus.filter(is_deposit = '1')

    lang = translation.get_language()
    country = Countries.objects.get(slug = lang)

    countryPaysList = CasinoCountryPay.objects.filter(casino=casino)
    payCasinoList = casino.casinoCountryPay.filter(countries=country)

    context = {'casino': casino, 'games':games, 'gambler_id':gambler_id,  'bonus_no_deposit': bonus_no_deposit, 'bonus_deposit':bonus_deposit, 'country': country, 'countryPaysList': countryPaysList, 'payCasinoList':payCasinoList }
    return render(request, 'review.html', context)
    
@never_cache
def go(request, casino_slug):
    casino = get_object_or_404(Casino, slug=casino_slug)
    lang = translation.get_language()
    if request.GET:
        gambler_id = get_anid(request)
        param = 'anid=' + gambler_id + '&payload=' + gambler_id + '&clickid=' + gambler_id + '&s2s.req_id=' + gambler_id + '&gklid=' + gambler_id
    else:
        gambler_id=False
        param = False
    
    if not casino.link or casino.link == '#':
        link = casino.link_en
    else:
        link = casino.link
    
    if gambler_id and param:
        if 'http' in link:
            fulllink = link + '/?' + param
        else:
            fulllink = 'https://' + link + '/?' + param
    else:
        if 'http' in link:
            fulllink = link + '/'
        else:
            fulllink = 'https://' + link + '/'
    return redirect(fulllink)