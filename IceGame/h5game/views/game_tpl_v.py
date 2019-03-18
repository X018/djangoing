#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

from django.views import generic
from django.shortcuts import get_object_or_404

from ..models.game_tpl_m import GameTpl
from ..models.game_skin_m import GameSkin

from ..controller.fs_c import FileSysCtrl
from ..controller.svn_c import SvnCtrl



class GameTplView(generic.RedirectView):
    '''
    游戏跳转页面
    '''

    def get_redirect_url(self, *args, **kwargs):
        game = get_object_or_404(GameTpl, pk=kwargs['pk'])
        FileSysCtrl.sync_tpl_h5_engine(game.id)
        SvnCtrl.sync_game_tpl(game.id)
        return game.get_url()
        
