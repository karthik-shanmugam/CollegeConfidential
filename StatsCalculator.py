f=open('FinalData.txt','r')
i=0
order=['Cal','Stanford','UCLA','USC']
data=[[],[],[],[]]
Calfurd=[]
UCSC=[]
f.readline()
for line in f:
	numbers=line.split()
	i=0
	for number in numbers:
		data[i].append(int(number))
		i=i+1
for i in range(4):
	print(order[i]+': '+str(sum(data[i])))
for i in range(9998):
	Calfurd.append(data[0][i]-data[1][i])
	UCSC.append(data[2][i]-data[3][i])
import statistics
print('Cal-Stanford: mean= '+str(statistics.mean(Calfurd))+' stdev= '+str(statistics.stdev(Calfurd)))
print('UCLA-USC: mean= '+str(statistics.mean(UCSC))+' stdev= '+str(statistics.stdev(UCSC)))



