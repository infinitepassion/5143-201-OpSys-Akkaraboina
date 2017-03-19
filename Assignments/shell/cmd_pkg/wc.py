import sys
import os
"""
@Name: wc
@Description: Used to count number of lines/words/characters in file
@Params: cmd(list)
"""
def wc(cmd):
	os.system('touch output.txt')
	op_file=open("output.txt",'w')
	lines=0
	words=0
	chars=0
	if os.path.isfile(cmd[1]) :
		for line in open(cmd[1]).readlines(  ):
			lines=lines+1
			for word in line.split(  ):
				words=words+1
			chars=len(open(cmd[1],'r+').read())
		k=str(lines)+" "+str(words)+" "+str(chars)+" "+str(cmd[1])
		op_file.write(k)
		
	else :
		op_file.write("invalid file")
	op_file.close()
	return