import sys
import os
import shutil
import subprocess
"""
@Name: grep
@Description: search a file for keywords within a file
@Params: cmd(list) - file that will be searched
"""
def  grep(cmd):
	os.system('touch output.txt')
	op_file=open("output.txt",'w')
	if os.path.isfile(cmd[2]):
		search_term = cmd[1]
		file = cmd[2]
		# print(cmd[1])
		# print(cmd[2])
		c=0
		# if search_term in open(f).read():
			# print("true")
		with open(file) as f:
			for line in f:
				if search_term in line:
					op_file.write(line)
					c=1
		if c == 0:
			op_file.write("no matches found")
		op_file.close()
		f.close()
	else:
		op_file.write("no file found")
	op_file.close()
	return
