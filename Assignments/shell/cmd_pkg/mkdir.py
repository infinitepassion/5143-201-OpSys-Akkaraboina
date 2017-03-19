import os
import shutil
"""
@Name: mkdir
@Description: create directory
@Params: cmd(list) - to create a directory
"""
def mkdir(cmd):
	os.system('touch output.txt')
	path=[]
	# check for the valid path and create the directory
	if os.path.exists(cmd[1]):
		print ("dir exists")
	else:
		# if "/" not in cmd[1]:
			# path=os.getcwd()
			# # print path
			# path=path+"/"+cmd[1]
			# os.mkdir(path)
		# # if path is given this set of instructions will be exec
		# elif os.path.exists(cmd[1]) :
		path=cmd[1]
		# print(path)
		os.mkdir(path)
	return
