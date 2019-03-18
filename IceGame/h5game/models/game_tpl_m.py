#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

from .abs_game_m import AbsGame



class GameTpl(AbsGame):
	'''
	游戏模板类
	'''

	def is_template(self):
		'''
		是否为模板游戏
		'''
		return True



	def __str__(self):
		return '%s[%s]' % (self.project.name, self.name)
