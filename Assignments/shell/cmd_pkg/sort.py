import sys
import os
import shutil
"""
@Name: sort
@Description: sorting the data in the mentioned file
@Params: f_name(string) - sorting the data in the given file
"""
def sort(cmd):
	os.system('touch output.txt')
	# print(cmd[1])
	if os.path.isfile(cmd[1]):
		with open(cmd[1], 'r') as r:
			for line in sorted(r):
				print(line),
	else :
		print("sort: cannot read: No such file or directory")
	return