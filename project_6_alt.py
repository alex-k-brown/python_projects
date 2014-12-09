import string
import random
import collections


def id_generator(size=26, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


f = open("project_six.dat","w")
for _ in range(10):
    f.write(id_generator())
    f.write("\n")
f.close()

my_dictionary = dict()
f = open("project_six.dat", "r+")
count = 0
for line in f:
    for char in line.replace("\n",""):
        count += 1
        if char in my_dictionary:
            my_dictionary[char] += 1
        else:
            my_dictionary[char] = 1

print "num of characters: " + str(count)
for key in my_dictionary:
    print "%s --- %s" % (key, my_dictionary[key])
f.close()