import sys
import os

"""
@Name: cd
@Description: change to the named directory
@Params: cmd(list) - The path to be changed
"""
def cd(cmd):
	os.system("touch output.txt")
	op=open("output.txt",'r')
	if len(cmd)==1 :
		path=os.getenv("HOME")
		os.chdir(path)
		os.system("touch output.txt")
	else :
	#checking for '~' command in command line arguments if given by the user
		if cmd[1]=="~":
			path=os.getenv("HOME") #change to the home-directory
			os.chdir(path)
			os.system("touch output.txt")
	#checking for '..' command in command line argumentsuments if given by the user
		elif cmd[1]=="..":
			os.chdir("..") #changes to the parent directory
			os.system("touch output.txt")
		else :
			os.chdir(cmd[1])
			os.system("touch output.txt")
	op.close()
	return
