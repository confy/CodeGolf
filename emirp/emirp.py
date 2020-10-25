def prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            return 1
for i in range(999):
    if prime(i) is 1:
        r = str(i)[::-1]
        r = int(r)
        if prime(r) is 1 and r != i:
            print(i)