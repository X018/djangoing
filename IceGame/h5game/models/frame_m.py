#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import os

from django.db import models



class Frame(models.Model):
	'''
	框架数据类
	'''

	# 框架名
	name = models.CharField(max_length=200)
	# 项目目录
	root_dir = models.CharField(max_length=200, default='frame2/client')
	# 
	frame_dir = models.CharField(max_length=200, default='trunk')
	# 框架发布时间
	pub_time = models.DateTimeField('time published')


	def get_dir(self):
		return os.path.join(self.root_dir, self.frame_dir)


	def __str__(self):
		return self.name
