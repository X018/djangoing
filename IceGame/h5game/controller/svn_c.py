#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import os

from django.conf import settings

from ..models.frame_m import Frame
from ..models.game_tpl_m import GameTpl
from ..models.game_skin_m import GameSkin



class SvnCtrl(object):
    """
    文件控制管理类
    """

    @staticmethod
    def sync_frame(frame_id):
        '''
        同步更新框架
        '''
        frame_list = Frame.objects.filter(id=frame_id)
        frame = frame_list and frame_list[0] or None
        if frame is not None:
            os.system('svn up %s' % (os.path.join(settings.BASE_DIR, frame.get_dir())))


    @staticmethod
    def sync_game(game):
        '''
        同步更新游戏
        '''
        if game is not None:
            proj_game_dir = game.get_dir()
            os.system('svn up %s' % (os.path.join(settings.BASE_DIR, proj_game_dir)))


    @staticmethod
    def sync_game_tpl(tpl_id):
        '''
        同步更新模板游戏
        '''
        tpl_list = GameTpl.objects.filter(id=tpl_id)
        tpl = tpl_list and tpl_list[0] or None
        if tpl is not None:
            frame_id = tpl.project.frame.id
            SvnCtrl.sync_frame(frame_id)
            SvnCtrl.sync_game(tpl)
        return tpl


    @staticmethod
    def sync_game_skin(skin_id):
        '''
        同步更新换肤游戏
        '''
        skin_list = GameSkin.objects.filter(id=skin_id)
        skin = skin_list and skin_list[0] or None
        if skin is not None:
            SvnCtrl.sync_game(skin)
        return skin


    @staticmethod
    def sync_game_releated(game_id):
        '''
        同步更新模板游戏与换肤游戏
        '''
        game = SvnCtrl.sync_game_skin(game_id)
        if game is not None:
            SvnCtrl.sync_game_tpl(game.template.id)