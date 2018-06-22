import os,sys
r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()

if pid>0:
	print "In parent"
	os.close(r)
	parent=os.fdopen(w,'w')
	num=raw_input("Enter the list of numbers")
	parent.write(num)	
	parent.close()
	
else:
	print "In child process"
	os.close(w)
	child=os.fdopen(r)
	recvd1=child.read()
	num=recvd1.split()
	l=len(num)
	p=" "
	for i in range(l):
		no=int(num[i])
		if no%2==0:
			no=no*no
			p=p+str(no)+" "
	print "Child reading ",recvd1
	os.close(r1)
	child1=os.fdopen(w1,'w')
	child1.write(p)
	print "Child writing ",p
	child1.close()
	#sys.exit(0)
if pid>0:
	print "Hello"		
	os.close(w1)
	
	parent1=os.fdopen(r1)
	ans=parent1.read()
	print "Answer is ",ans
	parent1.close()
	sys.exit(0)
	
		
		
