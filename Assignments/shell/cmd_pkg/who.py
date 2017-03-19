import sys
import os
"""
@Name: who
@Description: displays the list of users currently logged in
@Params: None
"""
def  who():
	os.system('touch output.txt')
	op_file=open("output.txt",'w')
	op_file.write(os.popen('who').read())
	
	
