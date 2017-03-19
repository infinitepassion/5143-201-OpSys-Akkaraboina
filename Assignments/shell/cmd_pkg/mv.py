import sys
import os
import shutil
"""
@Name: mv
@Description: Used to rename a file
@Params: cmd(list) - the file to rename
"""	
def mv(cmd):
	os.system('touch output.txt')
	if len(cmd)==3:
		if os.path.isfile(cmd[1]):
		# copy the file and then remove original file
			shutil.copyfile(cmd[1], cmd[2])
			os.remove(cmd[1])
		else :
			print ("mv: cannot stat'"),
			print(cmd[1]),
			print("': No such file or directory")
	else:
		print "Invalid syntax"
	return