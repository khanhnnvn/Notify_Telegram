# -*- coding: utf-8 -*-
import requests
# import os
import config
import json
import time
import schedule
from bs4 import BeautifulSoup
import telegram_module
def check_port(host, port):
	import socket
	host=str(host)
	port=int(port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(10) 
	result = sock.connect_ex((host,port))
	if result == 0:
		mess="Ket noi toi "+host+":"+str(port)+" thanh cong"
		print(mess)
		return [1, mess]
	else:
		mess="Ket noi toi "+host+":"+str(port)+" that bai"
		telegram_module.telegram_send_to(config.chat_canhbao,str(mess),config.api_canhbao)
		print(mess)
		return [0, mess]
a = "pycon.vn"
b = 443
check_port(a, b)
#schedule.every(10).minutes.do(check_port(a, b))
if __name__ == '__main__':
	while True:
		try:
			
			check_port(a, b)
			#time.sleep(5)
		except Exception as value:
			print(value)
			pass
