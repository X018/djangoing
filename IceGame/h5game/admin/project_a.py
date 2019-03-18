#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import os
import sys

from django.contrib import admin

from ..models.project_m import Project



class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('项目配置', {'fields': ['name']}),
        (None, {'fields': ['frame']}),
        (None, {'fields': ['host']}),
        (None, {'fields': ['port']}),
        (None, {'fields': ['root_dir']}),

        ('发布时间', {'fields': ['pub_time']}),
    ]

    # 显示可选择的框架列表
    radio_fields = {"frame": admin.VERTICAL}


admin.site.register(Project, ProjectAdmin)
