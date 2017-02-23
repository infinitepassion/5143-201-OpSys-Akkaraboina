import sys
import os
import shutil
from stat import *
import time
import pwd
from os import walk
import grp

"""
@Name: ls
@Description: Used to display the files and directories depending upon option
@Params: f_name(string) - file to be displayed
"""
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
			if list[i]==list[i].lstrip('.'):
				text =  list[i]+"\t"
				op_file.write(text)
#checking for 'ls -a' command in command line arguments then displays the long listing of files in the directory based on the last access time of files.
	else: 
	# 1
		if cmd[1]=='-a': 
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				text =  list[i]+"\t" 
				op_file.write(text)
	#2
		elif cmd[1]=='-l':
			# w=os.popen('whoami').read()
			flag='-l'
			list1=[]
			list2=[]
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				if(i<len(list)):
					if list[i]!=list[i].lstrip('.'):
						if(i<len(list)):
							list.remove(list[i])
			for i in list:
				uid = os.stat(i).st_uid
				# uid = st.st_uid
				user=pwd.getpwuid( uid)
				w=user
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
								# print(k,Size,Perm,Atime)
								text=str(Perm)+"\t"+ str(w)+"\t"+str(Size)+"\t"+str(Atime)+"\t"+str(k) + "\n"
								op_file.write(text)
	#checking for 'ls -lh' command in command line arguments then displays the file according to human readable sizes
		# 3
		elif cmd[1]=='-h':
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				if list[i]==list[i].lstrip('.'):
					text =  list[i]+"\t"
				op_file.write(text)
		#4
		elif cmd[1]=='-ah':
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				if list[i]==list[i].lstrip('.'):
					text =  list[i]+"\t"
				op_file.write(text)
				#5
		elif cmd[1]=='-la':
			# w=os.popen('whoami').read()
			flag='-l'
			list1=[]
			list2=[]
			list=os.listdir(os.getcwd())
			for i in list:
				uid = os.stat(i).st_uid
				# uid = st.st_uid
				user=pwd.getpwuid( uid)
				w=user
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
								# print(k,Size,Perm,Atime)
								text=str(Perm)+"\t"+ str(w)+"\t"+str(Size)+"\t"+str(Atime)+"\t"+str(k) + "\n"
								op_file.write(text)
		# 6
		elif cmd[1]=='-lh':
			flag='-l'
			list1=[]
			list2=[]
			list=os.listdir(os.getcwd())
			for i in range(len(list)):
				if(i<len(list)):
					if list[i]!=list[i].lstrip('.'):
						if(i<len(list)):
							list.remove(list[i])
			for i in list:
				uid = os.stat(i).st_uid
				# uid = st.st_uid
				user=pwd.getpwuid( uid)
				w=user
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
								# print(k,Size,Perm,Atime)
								text=str(Perm)+"\t"+str( w)+"\t"+str(Size)+"\t"+str(Atime)+"\t"+str(k) + "\n"
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
				uid = os.stat(i).st_uid
				# uid = st.st_uid
				user=pwd.getpwuid( uid)
				w=user
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
								# print(k,Size,Perm,Atime)
								text=str(Perm)+"\t"+str( w)+"\t"+str(Size)+"\t"+str(Atime)+"\t"+str(k) + "\n"
								op_file.write(text)
	op_file.close()
	return


