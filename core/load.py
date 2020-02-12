import sys, time
def exit():
	for _ in range(2):
		for a in "-\|/":
			print ("\rExiting {}".format(a), flush=True, end="")
			time.sleep(0.1)
