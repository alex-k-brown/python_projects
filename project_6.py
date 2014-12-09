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

random_strings = open("project_six.dat").readlines()

for p in random_strings:
    print p, "A:", p.count("A"), "B:", p.count("B"), "C:", p.count("C"), "D:", p.count("D"), "E:", p.count("E"), "F:", p.count("F"), "G:", p.count("G"), "H:", p.count("H"), "I:", p.count("I"), "J:", p.count("J"), "K:", p.count("K"), "L:", p.count("L"), "J:", p.count("J"), "K:", p.count("K"), "L:", p.count("L"), "M:", p.count("M"), "N:", p.count("N"), "O:", p.count("O"), "P:", p.count("P"), "Q:", p.count("Q"), "R:", p.count("R"), "S:", p.count("S"), "T:", p.count("T"), "U:", p.count("U"), "V:", p.count("V"), "W:", p.count("W"), "X:", p.count("X"), "Y:", p.count("Y"), "Z:", p.count("Z"), "1:", p.count("1"), "2:", p.count("2"), "3:", p.count("3"), "4:", p.count("4"), "5:", p.count("5"), "6:", p.count("6"), "7:", p.count("7"), "8:", p.count("8"), "9:", p.count("9"), "\n"

