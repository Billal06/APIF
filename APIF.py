import sys, os, json
from optparse import OptionParser
if sys.version[0] == "2":
	print ("[INFO]> please use python3.x")
	sys.exit()
else:
	pass
from core import prompt as pr
from core import logger as log
from core import load
from core.help import help, show, main
from core.tools import *
def shell():
	while True:
		try:
			p = pr.prompt()
			if p == "exit":
				load.exit()
				print ()
				sys.exit()
			elif p == "help":
				help()
			elif p == "clear":
				os.system("clear")
			elif p == "about":
				about()
			elif p == "show":
				show()
			s = p.split(" ")
			if s[0] == "use":
				try:
					if s[1] == "localip":
						log.info("Your IP: "+localip())
					elif s[1] == "publicip":
						if publicip():
							log.info("Your IP: "+publicip())
						else:
							log.error("No Connection");sys.exit()
					elif s[1] == "getproxy":
						if getproxy():
							j = json.loads(getproxy())
							print ("[PROXY]> "+j["result"]["ip"]+":"+str(j["result"]["port"]))
						else:
							log.error("No Connection");sys.exit()
					elif s[1] == "user-agent":
						try:
							if getua(str(s[2])):
								j = json.loads(getua(str(s[2])))
								if j["status"] == "success":
									print ("[USER-AGENT]> {}".format(j["result"]["ua"]))
								else:
									log.error(j["pesan"])
							else:
								log.error("No Connection");sys.exit()
						except IndexError:
							print ("Usage: use [options] [browser]")
				except IndexError:
					print ("Usage: use [options]")
		except (EOFError,KeyboardInterrupt):
			print()
			log.error("please input 'exit' to exit tool")
			continue

def set():
	parser = OptionParser(add_help_option=False, epilog="API framework")
	parser.add_option("-s", help="Use Shell (Command Prompt / Terminal)", dest="shell", action="store_true")
	opt, args = parser.parse_args()
	if opt.shell == True:
		shell()
	else:
		main()

set()
