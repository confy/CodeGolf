for B in range(1,1001):
	A=''
	if B%2==0:A+='Foo' 
	if B%3==0:A+='Fizz'
	if B%5==0:A+='Buzz'
	if B%7==0:A+='Bar'
	if A=='':A=str(B)
	print(A)