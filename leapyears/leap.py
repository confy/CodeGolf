for i in range(1801, 2401):
    if i % 4 == 0 and (i % 400 == 0 or i % 100 != 0):
        print(i)
