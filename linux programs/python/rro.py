
n=int(raw_input("Enter no. of processes:"))
q=int(raw_input("Enter quantum time:"))

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


t=0
while min(done)==0:
	i=0
	
	while done[i]==1:
		i=i+1
	print i
	for l in range(i,n):
		if t<=arrt[l]:
			if prot1[l]<=q:
				t=arrt[l]+prot1[l]
				done[l]=1
				wait[l]=0
				prot1[l]=0
			else:
				t=arrt[l]+q
				prot1[l]=prot1[l]-q
		else:
			
				if done[l]!=1:
					if prot1[l]<=q:
						t=t+prot1[l]
						done[l]=1
						wait[l]=t-arrt[l]-prot[l]
						prot1[l]=0
					else:
						t=t+q
						prot1[l]=prot1[l]-q

for i in range(0,n):
	print "waiting time of process ",i+1,":",wait[i]					











