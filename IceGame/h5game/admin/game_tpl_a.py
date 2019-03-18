#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import os
import sys

from django.contrib import admin

from ..models.game_tpl_m import GameTpl



class GameTplAdmin(admin.ModelAdmin):

    fieldsets = [
        ('游戏配置', {'fields': ['project']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['game_dir']}),
        (None, {'fields': ['index_page']}),

        ('发布时间', {'fields': ['pub_time']}),
    ]

    # 显示可选择的项目列表
    radio_fields = {"project": admin.VERTICAL}


admin.site.register(GameTpl, GameTplAdmin)
