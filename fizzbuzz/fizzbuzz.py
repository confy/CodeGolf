for B in range(1,101):
	A=''
	if B%3==0:A+='Fizz'
	if B%5==0:A+='Buzz'
	if A=='':A=str(B)
	print(A)