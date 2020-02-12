import sys
def help():
	print ("""
Welcome to 'API Framework'

command:
   help         = show all commands (helping)
   show         = show all tools
   use [option] = use tools
   clear        = clear terminal
   about        = about this tool
   exit         = exit""")

def show():
	print ("""
Welcome to 'API Framework'

command:
   localip      = show local ip
   pubicip      = show public ip
   getproxy     = get random proxy""")

def main():
	print ("""
Welcome to 'API Framework'

Usage: {} [options]
Example: {} -s

Options:
   -s     = use shell or terminal""".format(sys.argv[0], sys.argv[0]))
