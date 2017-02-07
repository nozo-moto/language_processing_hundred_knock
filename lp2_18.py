# coding: utf-8
filename = 'hightemp.txt'
f = open(filename, 'r')
line = f.readlines()
f.close()

list_n = []
for i in range(0,len(line)-1):
    # list_n.append(float("".join(list(line[i].split("\t")[2]))))
    list_n.append(list(line[i].split("\t")))
sorted(list_n, key=lambda list:list_n[2])
print(list_n)
