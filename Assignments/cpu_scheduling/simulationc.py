#!/usr/bin/python3 
"""
Code is written in python
Execute command : python driver.py

"""

"""
@Program Name: SHELL
@Team: Ashoknaidu Gedela, Manju Yadav Akkaraboina, Sai Avinash Reddy Biradhavolu
@Description: 
	Implementation of  a program (in python) that simulates some of the job scheduling, CPU scheduling, and semaphore processing of an operating system.
"""
import glob  
import sys, os,shutil
from components import allfiles

if __name__ == '__main__':

	file_name1 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_c.txt'
	jobs_dict = allfiles.loadfile.load_process_file(file_name1,return_type="Dict")
	jobs_dict1=allfiles.loadfile.load_process_file(file_name1,return_type="Dict")
	max=0
	for key, value in jobs_dict.iteritems():
		key1=int(key)
		if key1>max:
			max=key1
	f = open('jobs_out.txt','a')
	sys.stdout = f
	allfiles.scheduling.scheduling(max,jobs_dict,jobs_dict1)
	f.close()
	shutil.move("jobs_out.txt", "input_data/jobs_out_c.txt")
	