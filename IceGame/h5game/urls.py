#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

from django.urls import path

from .views.index_v import IndexView
from .views.game_tpl_v import GameTplView
from .views.game_skin_v import GameSkinView


app_name = 'h5game'
urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('tpl/<int:pk>/', GameTplView.as_view(), name='tpl_view'),
    path('skin/<int:pk>/', GameSkinView.as_view(), name='skin_view'),
]