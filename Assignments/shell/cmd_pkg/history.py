import sys
import os
"""
@Name: history
@Description: Used to display list of executed commands in a particular session
@Params: list_history(list)
"""
def history(file):
	# read all the contents from the list_history for the history of commans that were executed in current shell session
	c=0
	fopen=open(file,'r')
	op_file=open("output.txt",'w')
	for lines in fopen:
		c=c+1
		line=str(c)+" "+lines
		op_file.writelines(line)
	op_file.close()
	return
