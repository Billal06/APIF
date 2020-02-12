import socket
import requests
import json
def localip():
	return socket.gethostbyname(socket.gethostname())

def publicip():
	try:
		r = requests.get("https://api.ipify.org")
		return r.text
	except requests.exceptions.ConnectionError:
		return False

def getproxy():
	try:
		r = requests.get("https://billal.herokuapp.com/api/freeproxy")
		j = json.loads(r.text)
		if j["status"] == "success":
			return r.text
		else:
			return False
	except requests.exceptions.ConnectionError:
		return False

def getua(browser):
		try:
			r = requests.get("https://billal.herokuapp.com/api/ua?browser="+browser)
		except requests.exceptions.ConnectionError:
			return False
