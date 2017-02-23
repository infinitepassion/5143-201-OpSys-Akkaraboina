#!/usr/bin/env python
"""
Code is written in python
Execute command : python shell.py

"""

"""
@Program Name: SHELL
@Team: Anusha Mongolu , Manju Yadav Akkaraboina, Swati Singh
@Description: 
	Implementation of "SHELL" in Python using the threads inorder to execute the each command in a thread.
"""

from cmd_pkg import commands
import threading
import sys
import string
import os
"""
	@Name: identify_cmd
	@Description: checking for the commands whether it is direct command or having redirect operators
	@Params: cmd(list)
	@Returns: None
	"""
def identify_cmd(cmd):
	history_open=open("history.txt",'a')
	cmd_copy=cmd
	cmd_copy=cmd_copy.split()
	history_open.write(cmd)
	history_open.write("\n")
	history_open.close()
	# list_history.append(cmd)
	while  cmd_copy[0] != "exit" :
	# or cmd_copy!=""):
# checking for '|' redirect operators if given by the user
		if '|' in cmd: 
			flag=1
			cmd=cmd.split('|')
			cmd[0]=cmd[0].strip()
			cmd[1]=cmd[1].strip()
			cmd1=str(cmd[0])
			cmd2=str(cmd[1])
			function(cmd1)
			p_file=open("output.txt",'r')
			p1_file=open("outputg.txt",'w')
			for line in p_file :
				p1_file.write(line)
			p_file.close()
			p1_file.close()
			new_cmd= cmd2 + " " + "outputg.txt"
			function(new_cmd)
			printfile = open("output.txt",'r')
			for line in  printfile:
				if line.rstrip():
					print(line)
		#checking for '>>' redirect operators if given by the user
		elif '>>' in cmd: # append standard output to a file
			cmd=cmd.split('>>')
			cmd[0]=cmd[0].strip()
			cmd[1]=cmd[1].strip()
			cmd1=str(cmd[0])
			cmd2=str(cmd[1])
			function(cmd1)
			if os.path.isfile(cmd2):
				outfile=open(cmd2,'a')
				infile=open("output.txt",'r')
				outfile.write("\n")
				for line in infile:
					outfile.write(line)
			else :
				print ("file doesn't exist")
			infile.close()
			outfile.close()
			os.system('touch output.txt') 
#checking for '>' redirect operators if given by the user
		elif '>' in cmd and len(cmd_copy)!=5 : #redirect standard output to a file
			cmd=cmd.split('>')
			cmd[0]=cmd[0].strip()
			cmd[1]=cmd[1].strip()
			cmd1=str(cmd[0])
			cmd2=str(cmd[1])
			function(cmd1)
			printfile = open("output.txt",'r')
			writefile=open(cmd2,'w')
			for line in  printfile:
				writefile.write(line) 
#checking for '<' redirect operators if given by the user
		elif '<' in cmd :
			flag=1
			cmd=cmd.split('<')
			cmd[0]=cmd[0].strip()
			cmd[1]=cmd[1].strip()
			if os.path.isfile(cmd[1]):
			# identify_cmd(cmd[1])
			# p_file=open("output.txt",'r')
			# p1_file=open("outputg.txt",'w')
			# for line in p_file :
				# p1_file.write(line)
			# p_file.close()
			# p1_file.close()
			# print( cmd[0]+ ' ' + cmd[1])
				os.system('touch output.txt') 
				identify_cmd (cmd[0]+ ' ' + cmd[1])
				c="rm output.txt"
				c=c.split()
				commands.rm.rm(c)
			else :
				print "invalid file"
			
		else :
			# os.system('touch output.txt')
			function(cmd)
			# print("printing")
			op=open("output.txt",'r')
			for line in op:
				if line.rstrip():
					print(line)
			op.close()
			c="rm output.txt"
			c=c.split()
			commands.rm.rm(c)
		cmd=raw_input("% ")
		cmd_copy=cmd
		history_open=open("history.txt",'a')
		history_open.write(cmd)
		history_open.write("\n")
		cmd_copy=cmd_copy.split()
		history_open.close()
	"""
	@Name: function
	@Description: Condition that drives the shell environment
	@Params: cmd(list)- checking for all the command
	@Returns: None
	"""
def function(cmd) :
	cmd=cmd.split()
	#checking for 'ls' command in command line arguments if given by the user
	if cmd[0]=='ls':
		t=threading.Thread(target=commands.ls.ls(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'mkdir' command in command line arguments if given by the user
	elif cmd[0] == 'mkdir':
		t=threading.Thread(target=commands.mkdir.mkdir(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'cd' command in command line arguments if given by the user
	elif cmd[0] == 'cd':
		t=threading.Thread(target=commands.cd.cd(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'pwd' command in command line arguments if given by the user
	elif cmd[0] == 'pwd':
		t=threading.Thread(target=commands.pwd.pwd())
		t.start()
		t.join()
	#checking for 'cp' command in command line arguments if given by the user
	elif cmd[0] == 'cp':
		t=threading.Thread(target=commands.cp.cp(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'mv' command in command line arguments if given by the user
	elif cmd[0] == 'mv':
		t=threading.Thread(target=commands.mv.mv(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'rm' command in command line arguments if given by the user
	elif cmd[0] == 'rm':
		# print(cmd[0],cmd[1])
		t=threading.Thread(target=commands.rm.rm(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'rmdir' command in command line arguments if given by the user
	elif cmd[0] == 'rmdir':
		t=threading.Thread(target=commands.rmdir.rmdir(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'cat' command in command line arguments if given by the user
	elif cmd[0] == 'cat':
		t=threading.Thread(target=commands.cat.cat(cmd),args=(cmd,))
		t.start()
		t.join()
		op_file=open("output.txt",'r')
	#checking for 'less' command in command line arguments if given by the user
	elif cmd[0] == 'less':
		t=threading.Thread(target=commands.less.less(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'head' command in command line arguments if given by the user
	elif cmd[0] == 'head':
		t=threading.Thread(target=commands.head.head(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'tail' command in command line arguments if given by the user
	elif cmd[0] == 'tail':
		line=0
		t=threading.Thread(target=commands.tail.tail(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'grep' command in command line arguments if given by the user
	elif cmd[0] == 'grep':
		t=threading.Thread(target=commands.grep.grep(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'wc' command in command line arguments if given by the user
	elif cmd[0] == 'wc':
		t=threading.Thread(target=commands.wc.wc(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'sort' command in command line arguments if given by the user
	elif cmd[0] == 'sort':
		t=threading.Thread(target=commands.sort.sort(cmd),args=(cmd,))
		t.start()
		t.join()
	#checking for 'history' command in command line arguments if given by the user
	elif cmd[0]=='history':
		file="history.txt"
		t13=threading.Thread(target=commands.history.history(file),args=(file,))
		t13.start()
		t13.join()
	#checking for 'chmod' command in command line arguments if given by the user
	elif cmd[0]=='chmod':
		t13=threading.Thread(target=commands.chmod.chmod(cmd),args=(cmd,))
		t13.start()
		t13.join()
	#checking for 'who' command in command line arguments if given by the user
	elif cmd[0]=='who':
		t=threading.Thread(target=commands.who.who())
		t.start()
		t.join()
	#checking for '!x' command in command line arguments if given by the user
	elif '!' in cmd[0] :
		if int(cmd[0].strip( '!')):
			hist_num=cmd[0]
			c=1
			os.system('touch output.txt')
			num=int(hist_num.strip( '!'))
			fopen=open("history.txt",'r')
			hist_cmd=""
			for i in fopen:
				if c==num:
					hist_cmd=i
					break
				else: 
					c=c+1
			identify_cmd(hist_cmd)
		else :
			os.system('touch output.txt')
			print "-bash: ",
			print cmd[0],
			print ": event not found"
	else:
		print("Invalid command")
		os.system('touch output.txt')
		
if __name__ == '__main__':
	cmd=raw_input("% ")
	identify_cmd(cmd)
	# history_open.write(cmd)
	

	