import pickle
x=pickle.load(open("testData - Copy.txt",'rb'))

Cal=['UCB']
f=open('FrequencyDataUCB.txt','w')
f.write("UCB")
total=0
for i in x:
	if i[0]:
		total=total+1
		
		berk=counts(i[0],i[1],Cal)
		f.write('\n'+berk)
f.close()
print (total)
