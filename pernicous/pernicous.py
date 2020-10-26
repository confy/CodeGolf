# this program is sort of a cheat, it does not search for primes but reads from a list.
prime_list = [2,3,5]
for i in range(51):
    binary = bin(i)[2:]
    count = binary.count('1')
    if count in prime_list:
        print(i)