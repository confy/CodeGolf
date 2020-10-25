for num in range(101):
    numstr = str(num)
    digit_sum = sum(int(char) for char in numstr)
    if num != 0 and num % digit_sum == 0:
        print(num)