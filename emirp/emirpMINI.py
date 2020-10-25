D=range
def C(n):
	if n>1:
		for A in D(2,n):
			if n%A==0:break
		else:return 1
for A in D(999):
	if C(A)is 1:
		B=str(A)[::-1];B=int(B)
		if C(B)is 1 and B!=A:print(A)