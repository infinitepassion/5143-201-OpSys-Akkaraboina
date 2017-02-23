import sys
import os
import shutil
import time
"""
@Name: less
@Description: Used to display first few lines of a file
@Params: cmd(list)
"""

"""
@Name: less
@Description: Used to display first few lines of a file
@Params: cmd(list)
"""
def less(cmd):
	os.system('touch output.txt')
	op_file=open("output.txt",'r')
	if os.path.isfile(cmd[1]):
		c=0
		lines=0
		# count num of lines in a file
		for line in open(cmd[1]).readlines():
			lines=lines+1
		c1=0
		file = open(cmd[1], "r")
		stop="\n"
		for line in file:
			if c1>lines:
				break
			else :
				print (line)
				c1=c1+1
				# print (c1)
				# print(c1%10)
				# print till 10 till ten lines and read the input character
				if c1%10==0:
					print("press enter to continue")
					key=raw_input()
					if key=="" :
						continue
					else:
						break
	# check if file doesn't exist
	else:
		op_file.write("No such file")
	return
