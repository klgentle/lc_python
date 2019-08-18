f=open('numbers.txt','r')
line=f.readline().strip()
sum = 0
while line != '':
    num=int(line)
    sum+=num
    line=f.readline()
f.close()
