# -*- coding:utf-8 -*-

"""
	阿里云API的调用, 参数： R：required， O：optional
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))
import requests
from hashlib import sha1
import hashlib
import hmac
import base64
import datetime


class mns:


	message = {
		"MessageBody": "",				# R 消息正文，XML格式
		"DelaySeconds":"0",				# O 指定的秒数延后可被消费
		"Priority":"8"					# O 指定消息的优先级权值，优先级越高的消息，越容易更早被消费
	}

	postdata = """
			<?xml version="1.0" encoding="UTF-8"?>
		    <Message xmlns="http://mns.aliyuncs.com/doc/v1/">
		        <MessageBody>{MessageBody}/MessageBody>
		        <DelaySeconds>{DelaySeconds}</DelaySeconds>
		        <Priority>{Priority}</Priority>
		    </Message>
			""".format(MessageBody="test", DelaySeconds="0", Priority="8")

	def postAPI(self,data):

		url = "https://1376489734199838.mns.cn-hangzhou.aliyuncs.com/queues/localtest/messages"
		

		m2 = hashlib.md5()   
		m2.update(data)   
		content = m2.hexdigest()
		GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
		# 生成datetime对象的过程和我可能不同，这里是拿当前时间来生成
		date = datetime.datetime.utcnow().strftime(GMT_FORMAT)
		signdata = "post + \n" + content + "\ntext/xml\n" + date + "\n" + url 
		signature = hmac.new('ZwnLQs3D1AdiTO6oilnrlPWGvnqKKx', str(signdata), sha1).digest()
		signature = base64.b64encode(signature)
		headers = {
			"Authorization": "MNS LTAIslNtcf4aU1Hz:" + signature,
			"Content-Length": len(str(data)),
			"Content-Type": "text/xml",
			"DATE": date,
			"x-mns-version": "2015-06-06"
		} 
		print headers
		print signature
		response = requests.post(url, data=data, headers=headers)
		return response

	def xmlTodict(self):
		"""解析返回结果"""
		pass

	def sendMessage(self, message):

		body = self.message
		body['MessageBody'] = message
		getdata = self.postdata
		# getdata = getdata.format(MessageBody=getdata['MessageBody'], DelaySeconds=getdata['DelaySeconds'], Priority=getdata['Priority'])
		response = self.postAPI(getdata)
		print response
		print response.text

	def receiveMessage(self):
		pass


a = mns()
a.sendMessage("ss")


