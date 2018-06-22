

n=int(raw_input("Enter no. of processes"))

arrt=[0]*n
prot=[0]*n
wait=[0]*n
turn=[0]*n

for i in range(0,n):
	print "Process:",i+1
	arrt[i]=int(raw_input('Enter arrival time of process'))
	prot[i]=int(raw_input('enter processing time'))


for i in range(0,n):
	for j in range(i,n-1):
		if arrt[j]>arrt[j+1]:
			temp=arrt[j]
			arrt[j]=arrt[j+1]
			arrt[j+1]=temp
			temp=prot[j]
			prot[j]=prot[j+1]
			prot[j+1]=temp

print "after sorting"		
for i in range(0,n):
	print "Process ",i+1,": burst time=",prot[i],",arrival time= ",arrt[i]		

t=0
for i in range(0,n):
	if t>=arrt[i]:
		wait[i]=t-arrt[i]
		t=t+prot[i]
	else:
		wait[i]=0
		t=arrt[i]+prot[i]
		

for i in range(0,n):
	turn[i]=wait[i]+prot[i]

avgw=0.0
avgt=0.0
for i in range(0,n):
	avgw=avgw+wait[i]
	avgt=avgt+turn[i]
avgw=avgw/n
avgt=avgt/n

for i in range(0,n):
	print "waiting time of process ",i+1,":",wait[i]
	print "turnaround time of process",i+1,":",turn[i]
print "average waiting time =",avgw
print "average turnaround time =",avgt



	
	
