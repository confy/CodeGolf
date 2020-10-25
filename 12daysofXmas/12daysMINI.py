F=range
B=print
C=['A Partridge in a Pear Tree.\n','Two Turtle Doves, and','Three French Hens,','Four Calling Birds,','Five Gold Rings,','Six Geese-a-Laying,','Seven Swans-a-Swimming,','Eight Maids-a-Milking,','Nine Ladies Dancing,','Ten Lords-a-Leaping,','Eleven Pipers Piping,','Twelve Drummers Drumming,']
D=['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth','Eleventh','Twelfth']
for A in F(12):
	B(f"On the {D[A]} day of Christmas\nMy true love sent to me")
	for E in F(A,-1,-1):B(C[E])