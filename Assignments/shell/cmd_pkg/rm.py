import sys
import os
"""
@Name: rm
@Description: Used to remove an existing file
@Params: cmd(list) - file to be removed
"""
def rm(cmd):
	os.system('touch output.txt')
	if os.path.isfile(cmd[1]) :
		os.remove(cmd[1])
	elif os.path.isdir(cmd[1]) :
		print("rm: cannot remove '"),
		print(cmd[1]),
		print("': Is a directory")
	else :
		print("rm: cannot remove '"),
		print(cmd[1]),
		print("': No such file or directory")
	return