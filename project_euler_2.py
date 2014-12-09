def fibo(prev1, prev2):
    total = 0
    error = 4000000
    num = prev1 + prev2
    while num <= 4000000:
        if num %2:
            total += num

    print total

fibo(2, 1)
