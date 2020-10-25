import time
B = " on the wall"
E = "Take one down and pass it around, "
e = ' bottles of beer'
R = ' bottle of beer'
for n in range(99, 1, -1):
    time.sleep(0.1)
    print(f"{n}{e}{B}, {n}{e}.")
    if n == 2:
        continue
    print(f"{E}{n-1}{e}{B}.\n")
print(f"{E}1{R}{B}.")
print(f"\n1{R}{B}, 1{R}.")
print(f"{E}no more{e}{B}.")
print(f"\nNo more{e}{B}, no more{e}.")
print(f"Go to the store and buy some more, 99{e}{B}.")
