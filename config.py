# -*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class defaultConfig():

	configs = []

	urls = {
		"huadong1": "http(s)://zhangbin2327.mns.cn-hangzhou.aliyuncs.com"

	}
	def __init__(self):

		# defaultConfig.configs.append(config)
		# print defaultConfig.configs
		pass

	# 阿里云消息队列 key 和 secret
	def aliyun(self):

		url = self.urls
		accessKey = "LTAIslNtcf4aU1Hz"
		accessSecret = "ZwnLQs3D1AdiTO6oilnrlPWGvnqKKx"
		
		return accessKey, accessSecret，url

