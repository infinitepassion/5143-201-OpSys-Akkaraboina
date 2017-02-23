import sys
import os
"""
@Name: wc
@Description: Used to count number of lines/words/characters in file
@Params: cmd(list)
"""
def wc(cmd):
	os.system('touch output.txt')
	lines=0
	words=0
	chars=0
	for line in open(cmd[1]).readlines(  ):
		lines=lines+1
		for word in line.split(  ):
			words=words+1
		chars=len(open(cmd[1],'r+').read())
	print("%d %d %d %s" %(lines,words,chars,cmd[1]))
	return