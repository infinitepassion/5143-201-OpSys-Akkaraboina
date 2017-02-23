import sys
import os
"""
@Name: chmod
@Description: Change the permission level(User, Group, Others) of files.
@Params:mode(int) - Octal number to set permissions for the user given file (Ex : 777, 755)
		cmd(list) - filename for which the permission level should be modified
"""
def chmod(cmd):
	os.system('touch output.txt')
	if os.path.exists(cmd[2]):
		str=cmd[1]
		num=int(str,8)
		os.chmod(cmd[2],num) #chmod() built-in functions to change the permission levels of a file
		# print( "Permissions changed successfully")
	else:
		print ("chmod: cannot access '"),
		print (cmd[1]),
		print ("': No such file or directory")
	return