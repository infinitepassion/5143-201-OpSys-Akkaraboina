import sys
import os
import shutil
import subprocess
"""
@Name: grep
@Description: search a file for keywords within a file
@Params: cmd(list) - file that will be searched
"""
def colorformatgrep(str):
	return '\033[31;1m' + str + '\033[0m'
def  grep(cmd):
	os.system('touch output.txt')
	op_file=open("output.txt",'w')
	if len(cmd) !=3:
		print "Invalid syntax"
	else:
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
						list=line
						list=list.split(search_term)
						str=""
						l=len(list)
						for i in range(len(list)-1):
							str= str+list[i]+colorformatgrep(search_term)
						str=str+list[l-1]
						op_file.write(str)
						c=1
			if c == 0:
				op_file.write("no matches found")
			op_file.close()
			f.close()
		else:
			op_file.write("no file found")
		op_file.close()
	return
