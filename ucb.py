import pickle
x=pickle.load(open("testData - Copy.txt",'rb'))

Cal=['UCB']
f=open('FrequencyDataUCB.txt','w')
f.write("UCB")
total=0
for i in x:
	if i[0]:
		total=total+1
		
		berk=str(i[0].count('UCB')+i[1].count('UCB'))
		f.write('\n'+berk)
f.close()
print (total)
