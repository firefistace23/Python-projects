n=int(raw_input('enter n'))
arr=[0]*n
for i in range(0,n):
	arr[i]=int(raw_input('enter no.'))

x=max(arr)
y=arr.index(max(arr))
print x
print y
