# coding: utf-8
filename = 'hightemp.txt'
f = open(filename, 'r')
line = f.readlines()
f.close()

for i in range(0,len(line)-1):
    print ((line[i].split("\t"))[0])
