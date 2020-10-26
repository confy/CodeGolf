p=[2,3,5]
for i in range(51):
	b=bin(i)[2:];c=b.count('1')
	if c in p:print(i)