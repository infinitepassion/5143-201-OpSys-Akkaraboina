# The entire simulation is handled in this file and it uses other modules from same pkg for handling different type of events.

import allfiles
def scheduling (max,jobs_dict,jobs_dict1):
	# All the list that are used in this program.
	Memory=512
	mem=[]
	memst=[]
	l1=[]
	l2=[]
	job_scheduling=[]
	cpu=[]
	io=[]
	iobt=[]
	iost=[]
	iopool=[]
	iokey=[]
	s0=[]
	s0st=[]
	s1=[]
	s1st=[]
	s2=[]
	s2st=[]
	s3=[]
	s3st=[]
	s4=[]
	s4st=[]
	sem=[1]*5
	finished=[]
	fstime=[]
	fctime=[]
	labels=['pid','atime','mreq','rtime','stime','ctime']
	ctime=0
	stime=0
	i=1
	ioflag=0
	flag=0
	l2stime=[]
	ajswt=0.0
	while i<=4*max:
		for key, value in jobs_dict.iteritems():
			key1=int(key)
			if key1==i:
				# Handling an process event
				if  'A' in  jobs_dict[key]['event']:
					m=int(jobs_dict[key]['mem_required'])
					if m<=512:
						job_scheduling.append(key)
					allfiles.eventa.eventa(m,key)
				# Handling an IO event
				elif 'I' in jobs_dict[key]['event']:
					allfiles.eventi.eventi(key)
					iopool.append(key)
					iobt.append(jobs_dict[key]['ioBurstTime'])
					if len(cpu)>0:
						io.append(cpu[0])
						iost.append(stime)
						iokey.append(key)
						# jobs_dict[cpu[0]]['burst_time']=(int(jobs_dict[cpu[0]]['burst_time']))-ctime
						if flag==0:
							jobs_dict[cpu[0]]['burst_time']=ctime
						else :
							jobs_dict[cpu[0]]['burst_time']=ctime+(int(jobs_dict[cpu[0]]['burst_time']))
						cpu.pop()
						
					# if len(iopool)==1 :
						# if len(cpu)>0:
							# io.append(cpu.pop())
							# ctime=int(jobs_dict[key]['ioBurstTime'])
						# else:
							# ctime=int(jobs_dict[iopool[0]]['ioBurstTime'])
							# cpu.append(iopool.pop())
					# Handling an display event
				elif 'D' in jobs_dict[key]['event']:
					allfiles.eventd.eventd(jobs_dict1,mem,l2,job_scheduling,'D',key,i,io,iokey,iobt,sem,s1,s2,s3,s4,s0,cpu,stime,ctime,finished,fstime,fctime,Memory,flag)
				# Handling an semaphore wait event
				elif 'W' in jobs_dict[key]['event']:
					print "Event:	W	Time:	",key
					s=jobs_dict[key]['semaphore']
					mflag=1
					if len(cpu)==0  and len(mem)==0:
						Memory=512
					while len(job_scheduling)>0 and mflag==1:
						key=job_scheduling[0]
						m=int(jobs_dict[key]['mem_required'])
						if( Memory-m>=0):
							Memory-=m
							ajswt+=i-int(jobs_dict1[job_scheduling[0]]['time'])
							mem.append(job_scheduling.pop(0))
							memst.append(0)
						else:
							mflag=0
					if len(cpu)==0:
						if len(mem)>0:
							ctime=int(jobs_dict[mem[0]]['burst_time'])
							if memst[0]==0:
								stime=i
								memst.pop(0)
							else:
								stime=memst.pop(0)
							
							cpu.append(mem.pop(0))
							if ctime>100:
								jobs_dict[cpu[0]]['burst_time']= ctime-100
								ctime=100
								flag='1'
						elif len(l2)>0:
							ctime=int(jobs_dict[l2[0]]['burst_time'])
							stime=l2stime.pop(0)
							cpu.append(l2.pop(0))
							if ctime>300:
								jobs_dict[cpu[0]]['burst_time']= ctime-300
								ctime=300
								flag='2'
					if s=='0':
						sem[0]-=1
						s0.append(cpu[0])
						s0st.append(stime)
						if flag==0:
							jobs_dict[cpu[0]]['burst_time']=ctime
						else :
							jobs_dict[cpu[0]]['burst_time']=ctime+(int(jobs_dict[cpu[0]]['burst_time']))
						cpu.pop()
					elif s=='1':
						sem[1]-=1
						s1.append(cpu[0])
						s1st.append(stime)
						if flag==0:
							jobs_dict[cpu[0]]['burst_time']=ctime
						else :
							jobs_dict[cpu[0]]['burst_time']=ctime+(int(jobs_dict[cpu[0]]['burst_time']))
						cpu.pop()
					elif s=='2':
						sem[2]-=1
						s2.append(cpu[0])
						s2st.append(stime)
						if flag==0:
							jobs_dict[cpu[0]]['burst_time']=ctime
						else :
							jobs_dict[cpu[0]]['burst_time']=ctime+(int(jobs_dict[cpu[0]]['burst_time']))
						cpu.pop()
					elif s=='3':
						sem[3]-=1
						s3.append(cpu[0])
						s3st.append(stime)
						if flag==0:
							jobs_dict[cpu[0]]['burst_time']=ctime
						else :
							jobs_dict[cpu[0]]['burst_time']=ctime+(int(jobs_dict[cpu[0]]['burst_time']))
						cpu.pop()
					elif s=='4':
						sem[4]-=1
						s4.append(cpu[0])
						s4st.append(stime)
						if flag==0:
							jobs_dict[cpu[0]]['burst_time']=ctime
						else :
							jobs_dict[cpu[0]]['burst_time']=ctime+(int(jobs_dict[cpu[0]]['burst_time']))
						cpu.pop()
				# Handling the semaphore release event
				elif 'S' in jobs_dict[key]['event']:
					print "Event:	S	Time:	",key
					s=jobs_dict[key]['semaphore']
					if s=='0' :
						if sem[0]>=1:
							sem[0]+=1
						else :
							sem[0]+=1
							mem.append(s0.pop(0))
							memst.append(s0st.pop(0))
					elif s=='1' :
						if sem[1]>=1:
							sem[1]+=1
						else :
							sem[1]+=1
							mem.append(s1.pop(0))
							memst.append(s1st.pop(0))
					elif s=='2' :
						if sem[2]>=1:
							sem[2]+=1
						else :
							sem[2]+=1
							mem.append(s2.pop(0))
							memst.append(s2st.pop(0))
					elif s=='3' :
						if sem[3]>=1:
							sem[3]+=1
						else :
							sem[3]+=1
							mem.append(s3.pop(0))
							memst.append(s3st.pop(0))
					elif s=='4' :
						if sem[4]>=1:
							sem[4]+=1
						else :
							sem[4]+=1
							mem.append(s4.pop(0))
							memst.append(s4st.pop(0))
		# Checking and reloading the level1 ready queue 
		mflag=1
		while len(job_scheduling)>0 and mflag==1:
			key=job_scheduling[0]
			m=int(jobs_dict[key]['mem_required'])
			if( Memory-m>=0):
				Memory-=m
				ajswt+=i-int(jobs_dict1[job_scheduling[0]]['time'])
				mem.append(job_scheduling.pop(0))
				memst.append(0)
				
			else:
				mflag=0
		# Checking the cpu status and loading the jobs from  ready queue
		if(len(cpu)==0):
			if len(mem)>0:
				ctime=int(jobs_dict[mem[0]]['burst_time'])
				if memst[0]==0:
					stime=i
					memst.pop(0)
				else:
					stime=memst.pop(0)
				
				cpu.append(mem.pop(0))
				if ctime>100:
					jobs_dict[cpu[0]]['burst_time']= ctime-100
					ctime=100
					flag='1'
			elif len(l2)>0:
				ctime=int(jobs_dict[l2[0]]['burst_time'])
				stime=l2stime.pop(0)
				cpu.append(l2.pop(0))
				if ctime>300:
					jobs_dict[cpu[0]]['burst_time']= ctime-300
					ctime=300
					flag='2'
			# Checking the cpu status and decrementing the clock cycles of cpu and terminating the jobs and demoting them to second level ready queue
		if len(cpu)==1:
			ctime-=1
			if ctime==0  and flag!='1' and flag!='2':
				print "Event:	T	Time:	",i+1
				Memory=Memory+int(jobs_dict[cpu[0]]['mem_required'])
				finished.append(cpu.pop())
				fstime.append(stime)
				fctime.append(i+1)
			# if ctime==0   and flag!='1' and flag!='2':
				# print "Event:	C	Time:	",i+1
				# flag=0
			if ctime==0 and (flag=='1' or  flag=='2'):
				# jobs_dict[cpu[0]]['burst_time']= ctime-100
				l2.append(cpu.pop())
				l2stime.append(stime)
				print "Event:	E	",
				print "Time: ",
				print i+1
				flag=0
				
			# Preempting the jobs from the IO to ready queue when the IO burst time is completed.
		for l in iopool:
			jobs_dict[l]['ioBurstTime']=int(jobs_dict[l]['ioBurstTime'])-1
		k=-1
		for l in iopool:
			if int(jobs_dict[l]['ioBurstTime'])==0:
				print "Event:	C	Time:	",i+1
				for ll in iokey:
					if l==ll:
						# print iokey,io,iost,k
						k=iokey.index(ll)
						iokey.remove(ll)
						mem.append(io.pop(k))
						memst.append(iost.pop(k))
					k+=1
		if (i==max):
			while len(s0)>0:
				mem.append(s0.pop(0))
				memst.append(s0st.pop(0))
				max=i+1500
			while len(s1)>0:
				mem.append(s1.pop(0))
				memst.append(s1st.pop(0))
				max=i+1500
			while len(s2)>0:
				mem.append(s2.pop(0))
				memst.append(s2st.pop(0))
				max=i+1500
			while len(s3)>0:
				mem.append(s3.pop(0))
				memst.append(s3st.pop(0))
				max=i+1500
			while len(s4)>0:
				mem.append(s4.pop(0))
				memst.append(s4st.pop(0))
				max=i+1500
			
		i=i+1
		# Calculating the totals and priting the final finished list 
	print "The contents of the FINAL FINISHED LIST"
	print"---------------------------------------"
	print "Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time"
	print "-----  ---------  ---------  --------  ----------  ---------"
	fc=fs=0
	att=0.0
	attd=0.0
	
	for r_time in finished:
		print jobs_dict1[r_time]['pid'],"	",r_time,"		",jobs_dict1[r_time]['mem_required'],"	",jobs_dict1[r_time]['burst_time'],"	",fstime[fs],"		",fctime[fc]
		att+=fctime[fc]-int(r_time)
		# ajswt+=int(fstime[fs])-int(jobs_dict1[r_time]['time'])
		attd+=1
		fc+=1
		fs+=1
	att=float(att/attd)
	ajswt=float(ajswt/attd)
	print
	print "The Average Turnaround Time for the simulation was ",att," units."
	print
	# 7344.376
	print "The Average Job Scheduling Wait Time for the simulation was ",ajswt," units."
	print
	print "There are ",
	print Memory,
	print " blocks of main memory available in the system."
	print 		
	return