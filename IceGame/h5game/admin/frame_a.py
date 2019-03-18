#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import os
import sys

from django.contrib import admin

from ..models.frame_m import Frame



class FrameAdmin(admin.ModelAdmin):
    fieldsets = [
        ('框架配置', {'fields': ['name']}),
        (None, {'fields': ['root_dir']}),
        (None, {'fields': ['frame_dir']}),

        ('发布时间', {'fields': ['pub_time']}),
    ]


admin.site.register(Frame, FrameAdmin)
