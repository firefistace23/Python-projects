
n=int(raw_input("Enter no. of processes"))

arrt=[0]*n
prot=[0]*n
prot1=[0]*n
wait=[0]*n
turn=[0]*n
done=[0]*n

for i in range(0,n):
	print "Process:",i+1
	arrt[i]=int(raw_input('Enter arrival time of process'))
	prot[i]=int(raw_input('enter processing time'))
	prot1[i]=prot[i]

'''for i in range(0,n):
	for j in range(0,n):
		if prot[j]>prot1[j+1]
		x=prot1[j]
		prot1[j]=prot1[j+1]
		prot1[j+1]=x'''


for i in range(0,n):
	for j in range(i,n-1):
		if arrt[j]>arrt[j+1]:
			temp=arrt[j]
			arrt[j]=arrt[j+1]
			arrt[j+1]=temp
			temp=prot[j]
			prot[j]=prot[j+1]
			prot[j+1]=temp
			temp=prot1[j]
			prot1[j]=prot1[j+1]
			prot1[j+1]=temp

print "after sorting"		
for i in range(0,n):
	print "Process ",i+1,": burst time=",prot[i],",arrival time= ",arrt[i]		

maxpt=max(prot)
t=0
for k in range(0,n):
	i=0
	while done[i]==1:
		i=i+1
	if arrt[i]>=t:
		wait[i]=0
		t=arrt[i]+prot[i]
		done[i]=1
		prot1[i]=maxpt
	else:
		l=prot1.index(min(prot1))
		wait[l]=t-arrt[l]
		t=t+prot[l]
		done[l]=1
		prot1[l]=maxpt
	
	
	

for i in range(0,n):
	print "waiting time of process ",i+1,":",wait[i]
			

			

	

			
		

