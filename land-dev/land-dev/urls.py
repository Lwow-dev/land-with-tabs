# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from casinos import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<slug:review_slug>/', views.show_review, name='review'),
    path('<slug:casino_slug>/go/', views.go, name='go'),
)