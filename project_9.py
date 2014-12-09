def newton(a,x):
    return (x + (a / x)) / 2


def my_sqrt(a, x):
    current_x = x
    next_x = newton(a, current_x)
    error = 0.000001
    iter_count = 1
    while abs(next_x - current_x) > error:
        current_x = next_x
        next_x = newton(a, current_x)
        iter_count += 1
    print "iterated " + str(iter_count) + " times"
    print next_x * 1.0

my_sqrt(9, 5)