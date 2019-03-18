#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import socket

from django.db import models

from .project_m import Project



class AbsGame(models.Model):
	'''
	游戏模板类
	'''

	# 游戏名
	name = models.CharField(max_length=200)
	# 游戏分支目录
	game_dir = models.CharField(max_length=200, default='')
	# 主页名
	index_page = models.CharField(max_length=200, default='index.html')
	# 游戏发布时间
	pub_time = models.DateTimeField('time published')

	# 游戏所属项目
	project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)


	class Meta:
		abstract = True


	def is_template(self):
		'''
		是否为模板游戏
		'''
		return False


	def get_name(self):
		'''
		获取游戏全名
		'''
		return '%s[%s]' % (self.project.name, self.name)


	def get_dir(self):
		'''
		获取游戏链接地址
		'''
		return '%s/%s' % (self.project.root_dir, self.game_dir)


	def get_url(self):
		'''
		获取游戏链接地址
		'''
		return '%s/%s/%s' % (self.project.get_url(), self.game_dir, self.index_page)


	# 
	def __str__(self):
		return self.name
