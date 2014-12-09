baseball_dic = {}
for line in open("baseball.dat"):
    line2 = line.split()
    name = ' '.join(line2[0:2])
    position = ' '.join(line2[2:5])
    baseball_dic[name] = position

print sorted(baseball_dic.items())