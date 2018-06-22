#Sooraj Eswaradas
#71

import os,sys
r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()
print "pid=",pid
if pid>0:
	#parent process
	os.close(r)
	ar=raw_input("enter the numbers : \n")
	#parent writing
	prnt=os.fdopen(w,'w')
	prnt.write(ar)
	print("Parent writing : "+ar)

	
else:
	#child process
	os.close(w)
	#child reading
	chld=os.fdopen(r)
	pr=chld.read()
	num=pr.split()
	l=len(num)
	p=" "
	for i in range(l):
		n=int(num[i])
        if n==2:
			p=p+str(n)+" "
		if n>1:	
			k=0
			for k in range(2,n):
				if n%k==0:
					break
			if k>n/2:
				p=p+str(n)+" "
	print("child reading : "+pr)

	#child process
	os.close(r1)
	#child writinging
	chld=os.fdopen(w1,'w')	
	chld.write(p)
	print("child writing back : "+p)
	sys.exit(0)
if pid>0:
	#parent process
	print "Soo"
	os.close(w1)
	#parent reading
	prnt=os.fdopen(r1)
	print "a"
	q=prnt.read()
	print "b"
	print("Parent reading : "+q)
	sys.exit(0)	 
		

	




