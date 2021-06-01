# uRequest.py

#-*- coding:utf-8 -*-

import requests

from datetime import datetime, timedelta

from frogmon.uCommon import COM
from frogmon.uGlobal import GLOB
from frogmon.uConfig import CONF
from frogmon.uLogger import LOG
from frogmon.uXml    import XMLPaser

class REQUEST():
	def getFireWarn(key, localArea):
		url = 'http://know.nifos.go.kr/openapi/forestPoint/forestPointListSearch.do'
		value = '?keyValue=%s&localArea=%s&excludeForecast=1' % (key, localArea)
		url = '%s%s' % (url, value)

		try:
			r = requests.get(url=url, timeout=3)
			print(r.url)
			print('--------------------')
			s = r.content.decode("UTF-8").strip()
			print(s)			
			return XMLPaser.decodeFireWarn(r.content)
		except:
			LOG.writeLn("[getFireWarn] Error : %s" % r.url)
			return None

	def updateSignal(metrixA, metrixB):
		if metrixA < 0 or metrixA > 1:
			exit()
		if metrixB < 0 or metrixB > 1:
			exit()

		phpFileNm = "swichin.php"
		url = 'http://58.229.176.179/'
		value = '?e_matrixa=%d&e_matrixb=%d' % (metrixA, metrixB)
		url = '%s%s%s' % (url, phpFileNm, value)

		try:
			r = requests.get(url=url, timeout=3)
			print(r.url)
			print('--------------------')
			s = r.content.decode("UTF-8").strip()
			print(s)			
		except:
			LOG.writeLn("[updateSignal] Error : %s" % r.url)
