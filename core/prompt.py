import readline
def prompt(default=1, path=None):
	p = ""
	if default == int(1):
		if not path:
			p = input("APIF >> ")
		else:
			p = input("APIF/%s >> "%(path))
	return p
