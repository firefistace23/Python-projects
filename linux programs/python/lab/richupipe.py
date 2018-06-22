import os,sys
r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()
if pid>0:
	os.close(r)
	prnt=os.fdopen(w,'w')
	ar=raw_input("enter the numbers")
	prnt.write(ar)
	print ("parent writing"+ar)
else:
	os.close(w)
	child=os.fdopen(r)
	pr=child.read()
	print ("child readig"+pr)
	os.close(r1)
	child1=os.fdopen(w1,'w')
	child1.write(pr)
	print ("child writing"+pr)
	sys.exit(0)
if pid>0:
	os.close(w1)
	prnt=os.fdopen(r1)
	q=prnt.read()
	print ("prnt reading"+q)
	sys.exit(0)	

