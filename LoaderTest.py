import pickle
x=pickle.load(open("testData - Copy.txt",'rb'))
counts = [[0 for y in range(12)]for z in range(13)]
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
toSearch=['Cal','UCB','Berkeley','Cali','oCal','rCal']
for i in x:
	found = False
	index = 0
	while found==False:
		if months[index] in i[2]:
			found=True
			counts[0][index]=counts[0][index]+1
			for j in range(len(toSearch)):
				temp=i[0]+i[1]
				counts[j+1][index]=counts[j+1][index]+temp.count(toSearch[j],0,len(temp))
		else:
			index=index+1
			if index==12:
				#print (i)
				found=True
for i in range(12):
	t=str(counts[0][i])
	output=months[i]+': '+' '*(9-len(months[i]))+t+' '*(4-len(t))+" threads"
	for j in range(len(toSearch)):
		temp=str(counts[j+1][i])
		output=output+', '+temp+' '*(3-len(temp))+' '+toSearch[j]
	print(output)
for i in range(12):
	output=(months[i])
	temp=0
	for j in range (1,len(toSearch)-3):
		temp+=counts[j][i]
	temp-=counts[4][i]
	temp-=counts[5][i]
	temp-=counts[6][i]	
	output+=': '+str(temp)
	print(output)

#print(x[4110][0])
#print(x[4110][1])
