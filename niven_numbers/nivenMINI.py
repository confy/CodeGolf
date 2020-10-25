for A in range(101):
	B=str(A);C=sum((int(A)for A in B))
	if A!=0 and A%C==0:print(A)