for A in range(1801, 2401):
    if A % 4 == 0 and (A % 400 == 0 or A % 100 != 0):
        print(A)
