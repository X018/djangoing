#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import os
import shutil

from django.conf import settings

from ..models.frame_m import Frame
from ..models.game_tpl_m import GameTpl
from ..models.game_skin_m import GameSkin

from ..config.game_conf import GameConf


class FileSysCtrl(object):
    """
    文件控制管理类
    """

    @staticmethod
    def copy_h5_engine(game_dir, frame_dir):
        '''
        拷贝H5引擎代码
        '''
        h5_engine_path = os.path.join(settings.BASE_DIR, frame_dir, GameConf.ENGINE_H5_DIR)
        game_h5_path = os.path.join(settings.BASE_DIR, game_dir, GameConf.ENGINE_H5_DIR)
        if not os.path.exists(game_h5_path):
            shutil.copytree(h5_engine_path, game_h5_path)


    @staticmethod
    def sync_game_h5_engine(game):
        '''
        同步更新模板游戏
        '''
        if game is not None:
            frame_id = game.project.frame.id
            frame_list = Frame.objects.filter(id=frame_id)
            frame = frame_list and frame_list[0] or None
            if frame is not None:
                FileSysCtrl.copy_h5_engine(game.get_dir(), frame.get_dir())


    @staticmethod
    def sync_tpl_h5_engine(tpl_id):
        '''
        同步更新模板游戏
        '''
        tpl_list = GameTpl.objects.filter(id=tpl_id)
        tpl = tpl_list and tpl_list[0] or None
        FileSysCtrl.sync_game_h5_engine(tpl)


    @staticmethod
    def sync_skin_h5_engine(skin_id):
        '''
        同步更新模板游戏
        '''
        skin_list = GameSkin.objects.filter(id=skin_id)
        skin = skin_list and skin_list[0] or None
        FileSysCtrl.sync_game_h5_engine(skin)


    @staticmethod
    def sysn_skin_from_tpl(skin_id, tpl_id):
        tpl_list = GameTpl.objects.filter(id=tpl_id)
        tpl = tpl_list and tpl_list[0] or None
        if tpl is not None:
            skin_list = GameSkin.objects.filter(id=skin_id)
            skin = skin_list and skin_list[0] or None
            if skin is not None:
                pass

