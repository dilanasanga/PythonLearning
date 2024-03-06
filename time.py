import time

def countdown(t):
	while t:
#		mins, secs = divmod(t, 60)
		mins = t//60
		secs = t%60
		timer = '{:02d}:{:02d}'.format(mins,secs)
		print(timer, end='\r')
		time.sleep(1)
		t = t-1
	print ("Countdonw complete")
t = input("Input time in seconds: ")
countdown(int(t))
