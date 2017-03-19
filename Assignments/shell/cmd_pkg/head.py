import sys
import os
import shutil
"""
@Name: head
@Description: Used to display first few lines of a file
@Params: cmd(list) - file to be displayed
"""
def head(cmd):
	os.system('touch output.txt')
	c=0
	if os.path.isfile(cmd[1]):
		file = open(cmd[1], "r")
		for line in file:
			print (line) #prints the number of lines in a given file
			c=c+1
			if c==20:
				break
		file.close()
	else :
		print ("head: cannot stat'"),
		print(cmd[1]),
		print("': No such file or directory")
	return