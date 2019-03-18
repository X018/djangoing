#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  


from django.db import models

from .abs_game_m import AbsGame
from .game_tpl_m import GameTpl



class GameSkin(AbsGame):
	'''
	游戏数据类
	'''

	# 游戏引用模板
	template = models.ForeignKey(GameTpl, default='', on_delete=models.DO_NOTHING)
	

	def get_url(self):
		'''
		获取游戏链接地址
		'''
		return '%s/%s/%s' % (self.project.get_url(), self.game_dir, self.index_page)


	def __str__(self):
		return '%s[%s]' % (self.project.name, self.name)
