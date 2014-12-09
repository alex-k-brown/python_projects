def frange(start, stop, increment):
    while start < stop:
        yield start
        start += increment

f = frange(0, 4, .5)

for n in f:
    print n
