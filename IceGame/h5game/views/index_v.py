#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

from itertools import chain

from django.views import generic

from ..models.game_tpl_m import GameTpl
from ..models.game_skin_m import GameSkin



class IndexView(generic.ListView):
    '''
    主页面
    '''

    template_name = 'h5game/index.html'
    context_object_name = 'game_list'


    def get_queryset(self):
        tpls = GameTpl.objects.order_by('-id')
        skins = GameSkin.objects.order_by('-id')
        return chain(tpls, skins)


