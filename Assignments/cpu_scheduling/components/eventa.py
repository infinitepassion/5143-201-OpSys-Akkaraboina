# Used for handling the processes in the simulation
#!/usr/bin/python3 
import glob  
import sys, os
def eventa(mem,key):
	if mem>512:
		print "Event:	A	Time:	",key
		print "This job exceeds the system's main memory capacity."
	else :
		print "Event: 	A	Time:	",key
	return