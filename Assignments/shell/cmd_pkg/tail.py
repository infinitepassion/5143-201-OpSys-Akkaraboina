import sys
import os
import shutil
"""
@Name: tail
@Description: Used to display last few lines of a file
@Params: cmd(list) - file to be displayed
"""
def tail(cmd):
	os.system('touch output.txt')
	p_file=open("output.txt",'w')
	lines=0
	if os.path.isfile(cmd[1]):
		for line in open(cmd[1]).readlines():
			lines=lines+1
		file = open(cmd[1], "r")
		print lines
		# if lines<20:
			# for line in file:
				# print(line)
		# elif lines<40:
			# i=lines%20
			# j=lines-i
			# k=0
			# for line in file:
				# if k<j:
					# k=k+1
				# else:
					# print(line)
		# else:
			# l=lines-20
			# m=0
			# for line in file:
				# if m<l:
					# m=m+10
				# else:
					# print(line)
		c=30
		op_file=open(cmd[1],'r')
		for line in op_file:
			if lines-c<=30:
				p_file.write(line)
				
				#print( line)
		
			else :
				lines=lines-1
				continue
		op_file.close()
	else:
		print ("tail: cannot stat'")
		print(cmd[1]),
		print("': No such file or directory")
	p_file.close()
	return