# -*- coding: utf-8 -*-
#author: か壞尐孩キ

from websocket import create_connection
import gzip
import time
import json
import hmac
import base64
import hashlib
import DataCollect.DataMem


def get_sign(secret_key, message):
	h = hmac.new(bytes(secret_key, 'utf-8'), bytes(message, 'utf-8'), hashlib.sha512)
	return base64.b64encode(h.digest())

class GateWs:
	def __init__(self, url, apiKey, secretKey):
		self.__url = url
		self.__apiKey = apiKey
		self.__secretKey = secretKey
		self.__dataMem = DataCollect.DataMem
		self.__MaxCycleSecs=600

	def gateGet(self,id,method,params):
		if(params==None):
			params=[]
		ws = create_connection(self.__url)
		data= { 'id' : id, 'method' : method, 'params' : params}
		js=json.dumps(data)
		ws.send(js)
		return ws.recv()

	def gateRequest(self,id,method,params):
		ws = create_connection(self.__url)
		nonce = int(time.time() * 1000)
		signature = get_sign(self.__secretKey, str(nonce))
		data= {'id': id, 'method': 'server.sign', 'params': [self.__apiKey, signature, nonce]}
		js=json.dumps(str(data))
		ws.send(js)
		if method == "server.sign":
			return ws.recv()
		else: 
			tmp=ws.recv()
			data= { 'id' : id, 'method' : method, 'params' : params}
			js=json.dumps(data)
			ws.send(js)
			tmp=ws.recv()
			return tmp

	def subGate(self,id,method,params):
		# the key store in redits
		strKey = ""
		recordBuffer ={}
		#construct the object of recordBuffer
		for tmp in params:
			recordBuffer[tmp]=[]

		#communicate with gate.io by websocket
		ws = create_connection(self.__url)
		nonce = int(time.time() * 1000)
		signature = get_sign(self.__secretKey, str(nonce))
		data= { 'id' : id, 'method' : 'server.sign' , 'params' : [self.__apiKey, signature, nonce]}
		js=json.dumps(str(data))
		ws.send(js)
		ws.recv()
		data = {'id': id, 'method': method, 'params': params}
		js = json.dumps(data)
		ws.send(js)

		#limit loop times for test
		count=99999999999999
		while (1):
			result = json.loads(ws.recv())
			if 'method' in result :
				#the response is the information of updated
				if result['method']=='trades.update':
					recordBuffer[result['params'][0]].append(result)
					#save trades in redits limit 600 records each currency pair
					if(len(recordBuffer[result['params'][0]])>self.__MaxCycleSecs):
						recordBuffer[result['params'][0]].pop(0)
					# save in redis
					strKey=result['params'][0]+'Buffer'
					self.__dataMem.setTmp(strKey, recordBuffer[result['params'][0]])
					print(result)
					#unsubscribe if times reached the limit
					count-=1
					if count<0:
						method='ticker.unsubscribe'
						data = {'id': id, 'method': method, 'params': params}
						js = json.dumps(data)
						ws.send(js)
						result = json.loads(ws.recv())
						if result['result']['status'] == 'success': return result
