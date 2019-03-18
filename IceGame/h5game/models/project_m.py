#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import socket

from django.db import models

from .frame_m import Frame



class Project(models.Model):
	'''
	项目数据类
	'''

	# 项目名
	name = models.CharField(max_length=200)
	# 项目链接IP
	host = models.CharField(max_length=200, default='', blank=True)
	# 项目链接端口
	port = models.CharField(max_length=200, default='8088', blank=True)
	# 项目目录
	root_dir = models.CharField(max_length=200, default='')
	# 项目发布时间
	pub_time = models.DateTimeField('time published')

	# 项目依赖框架
	frame = models.ForeignKey(Frame, on_delete=models.CASCADE,)


	def get_url(self):
		'''
		获取项目链接地址
		'''
		url = 'http://' + self.host
		if self.host == '':
			hostname = socket.gethostname()
			url += socket.gethostbyname(hostname)
		if self.port != '':
			url += (':' + self.port)
		return '%s/%s' % (url, self.root_dir)


	def __str__(self):
		return self.name
