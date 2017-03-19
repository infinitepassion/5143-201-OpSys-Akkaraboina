import sys
import os
import shutil
"""
@Name: rmdir
@Description: remove directory
@Params: cmd(list) - to remove a directory
"""
def rmdir(cmd):
	os.system('touch output.txt')
	
	path=os.getcwd()
	path=path+"/"+cmd[1]
	if os.path.exists(path):
		shutil.rmtree(cmd[1])
	else: 
		print("rmdir: failed to remove '"),
		print(cmd[1]),
		print("': No such file or directory")
	return
