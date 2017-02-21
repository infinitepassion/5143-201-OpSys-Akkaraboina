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
	cmd_copy=cmd
	cmd_copy=cmd_copy.split()
	list_history.append(cmd)
	while ( cmd_copy[0] != "exit"):
		#checking for '|' redirect operators if given by the user
		if '|' in cmd: # '|' pipe the output of command1 to the input of command
			flag=1
			cmd=cmd.split('|')
			cmd[0]=cmd[0].strip()
			cmd[1]=cmd[1].strip()
			cmd1=str(cmd[0])
			cmd2=str(cmd[1])
			function(cmd1)
			p_file=open("output.txt",'r')
			os.system('touch outputg.txt')
			p1_file=open("output.txt",'w')
			for line in p_file :
				p1_file.write(line)
			new_cmd= cmd2 + " " + "output.txt"
			function(new_cmd)
			p_file.close()
			p1_file.close()
		#checking for '>>' redirect operators if given by the user
		elif '>>' in cmd: # append standard output to a file
			cmd=cmd.split('>>')
			cmd[0]=cmd[0].strip()
			cmd[1]=cmd[1].strip()
			cmd1=str(cmd[0])
			cmd2=str(cmd[1])
			# print(cmd2)
			function(cmd1)
			if os.path.isfile(cmd2):
				outfile=open(cmd2,'a')
				infile=open("output.txt",'r')
				append=infile.read()
				outfile.write(append)
			else :
				print ("file doesn't exist")
			infile.close()
			outfile.close()
		#checking for '>' redirect operators if given by the user
		elif '>' in cmd and len(cmd_copy)!=5 : #redirect standard output to a file
			flag=1
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
		elif '<' in cmd : #redirect standard input from a file
			flag=1
			cmd=cmd.split('<')
			cmd[0]=cmd[0].strip()
			cmd[1]=cmd[1].strip()
			new_cmd=cmd[0]+ " "+cmd[1]
			# print(new_cmd)
			function(new_cmd)
			op=open("output.txt",'r')
			for line in op:
				print(line)
			op.close()
			c="rm output.txt"
			c=c.split()
			commands.rm.rm(c)
			
		else :
			# print(cmd)
			# os.system('touch output.txt')
			function(cmd)
			# print("printing")
			op=open("output.txt",'r')
			for line in op:
				print(line)
			op.close()
			c="rm output.txt"
			c=c.split()
			commands.rm.rm(c)
			
		print("% ",end='')
		cmd=input()
		list_history.append(cmd)
		cmd_copy=cmd
		cmd_copy=cmd_copy.split()
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
		t13=threading.Thread(target=commands.history.history(list_history),args=(list_history,))
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
	elif '!' in cmd[0]:
		hist_num=cmd[0]
		os.system('touch output.txt')
		num=int(hist_num.strip( '!'))
		print (list_history[num])
		identify_cmd(list_history[num-1])
	else:
		print("Invalid command")
		os.system('touch output.txt')
		
if __name__ == '__main__':
	list_history=[]
	print("% ",end='')
	cmd=input()
	identify_cmd(cmd)