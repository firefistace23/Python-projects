import os,sys
r,w=os.pipe()
pid=os.fork()
print "pid=",pid
if pid:
	#parent process
	os.close(r)
	prnt=os.fdopen(w,'w')
	print"parent is writing"
	n=raw_input("enter the numbers :")
	
	print ("parent writing"+n)
	prnt.write(n)
	#sys.exit(0)
else:
	#child process
	
	os.close(w)
	chld=os.fdopen(r)
	
	receved=chld.read()
	print "Child"
	print ("child is reading:"+receved)
	#sys.exit(0)
