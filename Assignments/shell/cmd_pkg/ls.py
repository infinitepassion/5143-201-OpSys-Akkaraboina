import sys
import os
import shutil
from stat import *
import time
from  pwd import getpwuid
from os import stat
# from cmd_pkg import perm_dict
import grp 


"""
@Name: ls
@Description: Used to display the files and directories depending upon option
@Params: f_name(string) - file to be displayed
"""
def colorformat(str):
	return '\033[32;1m' + str + '\033[0m'

def colorformatdir(str):
	return '\033[34;1m' + str + '\033[0m'
def perm_dict(val):
	dict={7:'rwx',6:'rw-',5:'r-x',4:'r--',3:'-wx',2:'-w-',1:'--x'}
	s=str(val)
	new_val=""
	for i in dict:
		if int(s[0]) == i:
			new_val=dict[i]
	for i in dict:
		if int(s[1])== i:
			new_val=new_val+dict[i]
	for i in dict:
		if int(s[2]) == i:
			new_val=new_val+dict[i]
	return new_val

# function to convert the size of file to human readable format
def convert_bytes(num):
	"""
	this function will convert bytes to MB.... GB... etc
	"""
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return "%3.1f %s" % (num, x)
		num /= 1024.0

def ls(cmd):
	os.system('touch output.txt')
	op_file=open("output.txt",'w')
	# print with no flags to ls
	if len(cmd)==1:
		list=os.listdir(os.getcwd())
		for i in range(len(list)):
				if(i<len(list)):
					if list[i]!=list[i].lstrip('.'):
						if(i<len(list)):
							list.remove(list[i])
		list.sort()
		for i in range(len(list)):
			if os.path.isdir(list[i]):
				list[i]=colorformatdir(list[i])
			else:
				list[i]=colorformat(list[i])
			op_file.write(list[i])
			op_file.write('\t')
#checking for 'ls -a' command in command line arguments then displays the long listing of files in the directory based on the last access time of files.
	else: 
	# 1
		if cmd[1]=='-a': 
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				
				# text =  list[i]+"  " 
				if os.path.isdir(list[i]):
					list[i]=colorformatdir(list[i])
				else:
					list[i]=colorformat(list[i])
				op_file.write(list[i])
				op_file.write('\t')
	#2
		elif cmd[1]=='-l':
			flag='-l'
			list1=[]
			list2=[]
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				if(i<len(list)):
					if list[i]!=list[i].lstrip('.'):
						if(i<len(list)):
							list.remove(list[i])
			list.sort()
			for i in list:
				w=getpwuid(stat(i).st_uid).pw_name
				f=os.stat(os.getcwd()+"/%s"%i)
				if flag=='-la':
						list1.append(f.st_atime)
				elif flag=='-l':
						list1.append(f)
				list2.append(f)
			list1.sort()
			for i in range(0,len(list1)):
				for k in list:
						f=os.stat(os.getcwd()+"/%s"%k)
						st1=os.stat(k)
						if flag=='-la':
								temp1=f.st_atime
						elif flag=='-l':
								temp1=list2[0]
						if list1[i]==temp1:
								Size=f.st_size
								Perm=int(oct(os.stat(k)[ST_MODE])[-3:])
								Atime=time.asctime(time.localtime(st1[ST_ATIME]))
								perm_str=perm_dict(Perm)
								if os.path.isdir(k):
									k=colorformatdir(k)
									perm_str='d'+perm_str
								else:
									k=colorformat(k)
									perm_str='-'+perm_str
								text=str(perm_str)+"  "+ str(w)+"  "+str(Size)+"  "+str(Atime)+"  "+str(k) + "\n"
								op_file.write(text)
	#checking for 'ls -lh' command in command line arguments then displays the file according to human readable sizes
		# 3
		elif cmd[1]=='-h':
			list=os.listdir(os.getcwd())
			list.sort()
			for i in range(len(list)):
				if(i<len(list)):
					if list[i]!=list[i].lstrip('.'):
						if(i<len(list)):
							list.remove(list[i])
			for i in range(len(list)):
				if os.path.isdir(list[i]):
					list[i]=colorformatdir(list[i])
				else:
					list[i]=colorformat(list[i])
				op_file.write(list[i])
				op_file.write('\t')
		#4
		elif cmd[1]=='-ah':
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				
				# text =  list[i]+"  " 
				if os.path.isdir(list[i]):
					list[i]=colorformatdir(list[i])
				else:
					list[i]=colorformat(list[i])
				op_file.write(list[i])
				op_file.write('\t')
				#5
		elif cmd[1]=='-la':
			flag='-l'
			list1=[]
			list2=[]
			list=os.listdir(os.getcwd())
			for i in list:
				w=getpwuid(stat(i).st_uid).pw_name
				f=os.stat(os.getcwd()+"/%s"%i)
				if flag=='-la':
						list1.append(f.st_atime)
				elif flag=='-l':
						list1.append(f)
				list2.append(f)
			list1.sort()
			for i in range(0,len(list1)):
				for k in list:
						f=os.stat(os.getcwd()+"/%s"%k)
						st1=os.stat(k)
						if flag=='-la':
								temp1=f.st_atime
						elif flag=='-l':
								temp1=list2[0]
						if list1[i]==temp1:
								Size=f.st_size
								Perm=int(oct(os.stat(k)[ST_MODE])[-3:])
								Atime=time.asctime(time.localtime(st1[ST_ATIME]))
								perm_str=perm_dict(Perm)
								if os.path.isdir(k):
									k=colorformatdir(k)
									perm_str='d'+perm_str
								else:
									k=colorformat(k)
									perm_str='-'+perm_str
								text=str(perm_str)+"  "+ str(w)+"  "+str(Size)+"  "+str(Atime)+"  "+str(k) + "\n"
								op_file.write(text)
		# 6
		elif cmd[1]=='-lh':
			flag='-l'
			list1=[]
			list2=[]
			list=os.listdir(os.getcwd())
			for i in list:
				w=getpwuid(stat(i).st_uid).pw_name
				f=os.stat(os.getcwd()+"/%s"%i)
				if flag=='-la':
						list1.append(f.st_atime)
				elif flag=='-l':
						list1.append(f)
				list2.append(f)
			list1.sort()
			for i in range(len(list)):
				if(i<len(list)):
					if list[i]!=list[i].lstrip('.'):
						if(i<len(list)):
							list.remove(list[i])
			for i in range(0,len(list1)):
				for k in list:
						f=os.stat(os.getcwd()+"/%s"%k)
						st1=os.stat(k)
						if flag=='-la':
								temp1=f.st_atime
						elif flag=='-l':
								temp1=list2[0]
						if list1[i]==temp1:
								Size=convert_bytes(f.st_size)
								Perm=int(oct(os.stat(k)[ST_MODE])[-3:])
								Atime=time.asctime(time.localtime(st1[ST_ATIME]))
								perm_str=perm_dict(Perm)
								if os.path.isdir(k):
									perm_str='d'+perm_str
									k=colorformatdir(k)
								else:
									perm_str='-'+perm_str
									k=colorformat(k)
								text=str(perm_str)+"  "+str( w)+"  "+str(Size)+"  "+str(Atime)+"  "+str(k) + "\n"
								op_file.write(text)
								
		# checking for 'ls -l' command in command line arguments then displays the file according to with filename,
		# last access time, owner of filename and size of the file
		#7
		elif cmd[1]=='-lah':
			flag='-l'
			list1=[]
			list2=[]
			list=os.listdir(os.getcwd())
			for i in list:
				w=getpwuid(stat(i).st_uid).pw_name
				f=os.stat(os.getcwd()+"/%s"%i)
				if flag=='-la':
						list1.append(f.st_atime)
				elif flag=='-l':
						list1.append(f)
				list2.append(f)
			list1.sort()
			for i in range(0,len(list1)):
				for k in list:
						f=os.stat(os.getcwd()+"/%s"%k)
						st1=os.stat(k)
						if flag=='-la':
								temp1=f.st_atime
						elif flag=='-l':
								temp1=list2[0]
						if list1[i]==temp1:
								Size=convert_bytes(f.st_size)
								Perm=int(oct(os.stat(k)[ST_MODE])[-3:])
								Atime=time.asctime(time.localtime(st1[ST_ATIME]))
								perm_str=perm_dict(Perm)
								if os.path.isdir(k):
									perm_str='d'+perm_str
									k=colorformatdir(k)
								else:
									perm_str='-'+perm_str
									k=colorformat(k)
								text=str(perm_str)+"  "+str( w)+"  "+str(Size)+"  "+str(Atime)+"  "+str(k) + "\n"
								op_file.write(text)
	op_file.close()
	return


