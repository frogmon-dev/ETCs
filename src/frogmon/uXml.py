#uXml.py
from xml.etree import ElementTree

from frogmon.uCommon import COM
from frogmon.uConfig import CONF

class XMLPaser:
	def getHeader(content):
		xmlContents = content.decode("UTF-8").strip()#.replace("	","")
		#print('XML ---------------------')
		#print(xmlContents)
		#print('-------------------------')
		root        = ElementTree.fromstring(xmlContents)
		
		wHeader     = root.find("msgHeader")
		
		wHeaderCD   = wHeader.find("headerCd").text
		wHeaderMsg  = wHeader.find("headerMsg").text
		wOpcode     = wHeader.find("opcode").text
	
		if (wHeaderCD != 0):
			print('header Message : %s' % wHeaderMsg)
		
		return int(wHeaderCD)
		
	def decodeAction(content):
		xmlContents = content.decode("UTF-8").strip()#.replace("	","")
		#print('XML ---------------------')
		#print(xmlContents)
		#print('-------------------------')
		root        = ElementTree.fromstring(xmlContents)
		wBody       = root.find("msgBody")
		rc          = wBody.find("action").text
		#print(rc)
		return rc	
	
	def decodeWeather(content):
		rc = ['pty', 'sky', 'reh', 'rn1', 't1h', 'vec', 'wsd', 'lstupdt']
		xmlContents = content.decode("UTF-8").strip()
		#print('XML ---------------------')
		#print(xmlContents)
		#print('-------------------------')		
		root        = ElementTree.fromstring(xmlContents)		
		wBody       = root.find("msgBody")		
		rc[0]       = wBody.find("pty").text
		rc[1]       = wBody.find("sky").text
		rc[2]       = wBody.find("reh").text
		rc[3]       = wBody.find("rn1").text
		rc[4]       = wBody.find("t1h").text
		rc[5]       = wBody.find("vec").text
		rc[6]       = wBody.find("wsd").text
		rc[7]       = wBody.find("lstupdt").text		
		#print(rc)
		return rc	

	def decodeFireWarn(content, Area):
		rc = ['0', '0', '0', '0']
		xmlContents = content.decode("UTF-8").strip()
		#print('XML ---------------------')
		#print(xmlContents)
		#print('-------------------------')
		
		root        = ElementTree.fromstring(xmlContents)
		wBody       = root.find("outputData")
		
		for items in wBody:
			area = items.find("area").text
			if (area == Area):
				#print(items.find("sigun").text)
				meanavg     = items.find("meanavg").text
				val = float(meanavg)
				if val < 51:
					rc[0] = "%d" % round(val)
				elif val < 65:
					rc[1] = "%d" % round(val)
				elif val < 85:
					rc[2] = "%d" % round(val)
				else:
					rc[3] = "%d" % round(val)

		#print(rc)
		
		return rc			