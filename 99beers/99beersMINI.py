C=print
A=' on the wall'
E='Take one down and pass it around, '
B=' bottles of beer'
F=' bottle of beer'
for D in range(99,1,-1):
	C(f"{D}{B}{A}, {D}{B}.")
	if D==2:continue
	C(f"{E}{D-1}{B}{A}.\n")
C(f"{E}1{F}{A}.")
C(f"\n1{F}{A}, 1{F}.")
C(f"{E}no more{B}{A}.")
C(f"\nNo more{B}{A}, no more{B}.")
C(f"Go to the store and buy some more, 99{B}{A}.")