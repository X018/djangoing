#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import os
import sys

from django.contrib import admin

from ..models.game_skin_m import GameSkin



class GameSkinAdmin(admin.ModelAdmin):

    fieldsets = [
        ('游戏配置', {'fields': ['project']}),
        (None, {'fields': ['template']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['game_dir']}),
        (None, {'fields': ['index_page']}),

        ('发布时间', {'fields': ['pub_time']}),
    ]

    # 显示可选择的项目列表
    radio_fields = {"project": admin.VERTICAL, 'template': admin.VERTICAL}


admin.site.register(GameSkin, GameSkinAdmin)
