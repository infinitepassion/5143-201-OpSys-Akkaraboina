import sys
import os
import shutil
"""
@Name: cat
@Description: Displays a file
@Params: cmd(list) - The file to be displayed
"""
def cat(cmd):
	os.system('touch output.txt') 
	op_file=open("output.txt",'w')
	#checking for '>' in command line arguments if given by the user
	l=len(cmd)
	
	if ( l==2):
		for i in range(1,l):
			if os.path.isfile(cmd[i]): #if file found,open the file and read it
				openfile=open(cmd[i], 'r')
				for line in openfile:
					op_file.write(line)
				openfile.close()
				# op_file.write("\n")
			elif cmd[i]=='>' or cmd[i]== '>>':
				pass
			else :
				print ("file doesn't exist")
	
	elif cmd[3]=='>':
		if os.path.isfile(cmd[1]) and os.path.isfile(cmd[2]):
			filenames = [cmd[1], cmd[2]]
			with open(cmd[4], 'w') as outfile:
				for fname in filenames:
					with open(fname) as infile:
						for line in infile:
							outfile.write(line) #redirect the standard output to the file
			infile.close()
			outfile.close()
			op_file.close()
		else:
			print("Invalid files")
	else:
		print("Invalid syntax")
	op_file.close()
	return