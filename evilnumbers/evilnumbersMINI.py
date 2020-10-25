for A in range(51):
	B=str(bin(A))[2:];C=B.count('1')
	if C%2==0:print(A)