def myfun(a,d):
	for j in range((d)):
		first=a[0]
		for i in range(len(a)-1):
			a[i]=a[i+1]
			
		a[len(a)-1]=first
		
				
	return (a)
		
r=myfun([1,2,3,4,5],4)
print( '  '.join(map(str,r)))
