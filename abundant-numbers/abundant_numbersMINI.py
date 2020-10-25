C=range
for A in C(1,201):
	B=sum((B for B in C(1,A)if B is not A and A%B==0))
	if B>A:print(A)