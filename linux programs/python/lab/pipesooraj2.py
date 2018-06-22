import os,sys
r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()

if pid>0:
	os.close(r)
	ar=raw_input("Enter the set of numbers")
	wa=os.fdopen(w,'w')
	wa.write(ar)
	print "parent writing"
	wa.close()
	
else:
	os.close(w)
	ra=os.fdopen(r)
	recvd=ra.read()
	print "Received ",recvd
	num=recvd.split()
	l=len(num)
	p=" "
	for i in range(l):
		n=int(num[i])
		if n==2:
			p=p+str(n)+" "
		if n>1:	
			for i in range(2,n):
				if n%i==0:
					break
			if i>n/2:
					p=p+str(n)+" "
	print "Child reading",recvd
	os.close(r1)
	wb=os.fdopen(w1,'w')
	wb.write(p)
	print "Child writing back"
	sys.exit(0)
if pid>0:
	os.close(w1)
	rb=os.fdopen(r1)
	recvd2=rb.read()
	print "The prime numbers are ",recvd2
	rb.close()
	sys.exit(0)

			 
	
	
