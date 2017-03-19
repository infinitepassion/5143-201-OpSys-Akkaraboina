import sys
import os
"""
@Name: pwd
@Description: Used to get the current working directory
@Params: None
"""
def pwds():
	os.system('touch output.txt')
	op_file=open("output.txt",'w')
	op_file.write(os.getcwd())
	return