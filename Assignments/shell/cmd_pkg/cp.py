import sys
import os
import shutil  #imported the "shutil" library to use its built-in function

"""
@Name: cp
@Description: copy the file1 and call it the file2
@Params: cmd(list) - The file to be copying
"""
def cp(cmd):
	os.system('touch output.txt')
	if os.path.isfile(cmd[1]):
		shutil.copyfile(cmd[1], cmd[2])
	else :
		print ("cp: cannot stat'"),
		print(cmd[1]),
		print("': No such file or directory")
	return