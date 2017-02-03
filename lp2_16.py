# coding: utf-8
filename = 'hightemp.txt'
f = open(filename, 'r')
line = f.readlines()
f.close()

num = int(input())
i = 0
while(i<len(line)):
    for n in range(0, num):
        print(line[i+n])
    i += num
