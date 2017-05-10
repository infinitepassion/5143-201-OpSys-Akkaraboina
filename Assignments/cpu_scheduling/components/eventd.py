# Used for handling the display event in the simulation
#!/usr/bin/python3 

import subprocess,sys

display=[]
def eventd(jobs_dict1,l1,l2,temp,event_d,key,i,io,iokey,iobt,sem,s1,s2,s3,s4,s5,cpu,start_time,c_time,finished,fstime,fctime,Memory,flag):
	
	print "Event: ",
	print event_d,
	print "	",
	print "Time: ",
	print key
	print
	print "************************************************************"
	print
	print "The status of the simulator at time ",i,"."
	print  "The contents of the JOB SCHEDULING QUEUE"
	print "----------------------------------------"
	if len(temp)>0:
		print "Job #  Arr. Time  Mem. Req.  Run Time"
		print "-----  ---------  ---------  --------"
		print ""
		# for l in l1:
			# display.append(l)
		# for l in l2:
			# display.append(l)
		for l in temp:
			display.append(l)
		display.sort(key=int)
		for key in display:
			if key in jobs_dict1.keys():
				print jobs_dict1[key]['pid'],
				print "	",
				print jobs_dict1[key]['time'],
				print "	",
				print jobs_dict1[key]['mem_required'],
				print "	",
				print jobs_dict1[key]['burst_time']
		# print the file 
		del display[:]
	else :
		print
		print "The Job Scheduling Queue is empty."
		print
	print 
	print "The contents of the FIRST LEVEL READY QUEUE"
	print "-------------------------------------------"
	if (len(l1)==0):
		print
		print "The First Level Ready Queue is empty."
	else :
		print "Job #  Arr. Time  Mem. Req.  Run Time"
		print "-----  ---------  ---------  --------"
		for key in l1:
			if key in jobs_dict1.keys():
				print jobs_dict1[key]['pid'],
				print "	",
				print jobs_dict1[key]['time'],
				print "		",
				print jobs_dict1[key]['mem_required'],
				print "	",
				print jobs_dict1[key]['burst_time']
	print 
	print "The contents of the SECOND LEVEL READY QUEUE"
	print "--------------------------------------------"
	if (len(l2)==0):
		print
		print "The Second Level Ready Queue is empty."
	else :
		print "Job #  Arr. Time  Mem. Req.  Run Time"
		print "-----  ---------  ---------  --------"
		for key in l2:
			if key in jobs_dict1.keys():
				pid=jobs_dict1[key]['pid']
				print pid,
				print "	",
				print jobs_dict1[key]['time'],
				print "	",
				print jobs_dict1[key]['mem_required'],
				print "	",
				print jobs_dict1[key]['burst_time']
	print
	print "The contents of the I/O WAIT QUEUE"
	print "----------------------------------"
	if (len(io)==0):
		print 
		print "The I/O Wait Queue is empty."
	else :
		print
		print "Job #  Arr. Time  Mem. Req.  Run Time  IO Start Time  IO Burst  Comp. Time"
		print "-----  ---------  ---------  --------  -------------  --------  ----------"
		k=0
		for key in io:
			if key in jobs_dict1.keys():
				pid=jobs_dict1[key]['pid']
				print pid,
				print "	",
				print jobs_dict1[key]['time'],
				print "		",
				print jobs_dict1[key]['mem_required'],
				print "	",
				print jobs_dict1[key]['burst_time'],
				print "		",jobs_dict1[iokey[k]]['time'],
				print "	",jobs_dict1[iokey[k]]['ioBurstTime'],
				print "		",int(jobs_dict1[iokey[k]]['time'])+int(jobs_dict1[iokey[k]]['ioBurstTime'])
				k+=1
	print 
	print "The contents of SEMAPHORE ZERO"
	print "------------------------------"
	print "The value of semaphore 0 is ",sem[0],"."
	if len(s1)>0:
		for s in s1:
			print s
	else :
		print "The wait queue for semaphore 0 is empty."
	print
	print "The contents of SEMAPHORE ONE"
	print "-----------------------------"
	print "The value of semaphore 1 is ",sem[1],"."
	if len(s2)>0:
		for s in s2:
			print s
	else :
		print "The wait queue for semaphore 1 is empty."
	print		
	print "The contents of SEMAPHORE TWO"
	print "-----------------------------"
	print "The value of semaphore 2 is ",sem[2],"."
	if len(s3)>0:
		for s in s3:
			print s
	else :
		print "The wait queue for semaphore 2 is empty."
	print
	print "The contents of SEMAPHORE THREE"
	print "-------------------------------"
	print "The value of semaphore 3 is ",sem[3],"."
	if len(s4)>0:
		for s in s4:
			print s
	else :
		print "The wait queue for semaphore 3 is empty."
	print
	print "The contents of SEMAPHORE FOUR"
	print "------------------------------"
	print "The value of semaphore 4 is ",sem[4],"."
	if len(s5)>0:
		for s in s5:
			print s
	else :
		print "The wait queue for semaphore 4 is empty."
	print
	print "The CPU  Start Time  CPU burst time left"
	print "-------  ----------  -------------------"
	if len(cpu)>0:				
		for l in cpu:
			pid=jobs_dict1[l]['pid']
			print pid,
			print "		",
			print start_time,
			print "		",
			if flag!=1 or flag!=2:
				print c_time
			else :
				print jobs_dict1[l]['burst_time']
	else :
		print "The CPU is idle."
	print 
	print "The contents of the FINISHED  LIST"
	print"---------------------------------"
	print "Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time"
	print "-----  ---------  ---------  --------  ----------  ---------"
	fc=fs=0
	for r_time in finished:
		print jobs_dict1[r_time]['pid'],"	",r_time,"		",jobs_dict1[r_time]['mem_required'],"	",jobs_dict1[r_time]['burst_time'],"	",fstime[fs],"	",fctime[fc]
		fc+=1
		fs+=1
		print 
	print
	print "There are ",
	print Memory,
	print " blocks of main memory available in the system."
	