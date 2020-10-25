for i in range(51):
    binary_rep = str(bin(i))[2:]
    one_count = binary_rep.count('1')
    if one_count % 2 == 0:
        print(i)
