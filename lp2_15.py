# coding: utf-8
filename = 'hightemp.txt'
f = open(filename, 'r')
line = f.readlines()
f.close()

num = int(input())
for i in range (0, num):
    print (line[len(line)-i-1], end='')

#tail -n3 hightemp.txt
