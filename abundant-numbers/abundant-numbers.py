for num in range(1, 201):
    divisor_sum = sum(i for i in range(1, num) if i is not num and num % i == 0)
    if divisor_sum > num:
        print(num)