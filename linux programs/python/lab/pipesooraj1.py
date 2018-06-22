import sys,os
r,w=os.pipe()
pid=os.fork()

if pid>0:
	print "parent writing"
	os.close(r)
	w=os.fdopen(w,'w')
	n=raw_input("Enter the numbers")
	w.write(n)
	w.close()
	sys.exit(0)
else:
	os.close(w)
	print "Child reading"
	r=os.fdopen(r)
	recvd=r.read()
	print "The numbers entered are",recvd
	r.close()
	sys.exit(0)

