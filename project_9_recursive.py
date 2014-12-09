error = 0.000001
def newton(a,x):
    return (x + (a / x)) / 2

def recur2(a, current_x, next_x, count):
    if abs(next_x - current_x) <= error:
        return next_x, count
    else:
        count += 1
        return recur2(a, next_x, newton(a, next_x), count)

def recur1(a, x):
    current_x = x
    next_x = newton(a, current_x)
    result, count = recur2(a, current_x, next_x, 1)
    return result, count

sqrt, count = recur1(9, 7000,)
print "result: " + str(sqrt * 1.0) + " with " + str(count) + " times"