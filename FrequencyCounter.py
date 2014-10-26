def counts(data,data2,keys):
	total=0
	for key in keys:
		total+=data.count(key,0,len(data))
		total+=data2.count(key,0,len(data2))		
	return total
def addEndings(keys,endings,beginnings):
	newKeys=[]
	for key in keys:
		for ending in endings:
			for beginning in beginnings:
				newKeys.append(beginning+key+ending)
	return newKeys
	

import pickle
x=pickle.load(open("testData - Copy.txt",'rb'))
UCLA=['UCLA','ucla']
USC=['USC','University of Southern California','usc']
Cal=['Cal','Berkeley']
notCal=['Cal Tech','Cal tech','Cal State','Cal state','Berkeley College','Berkeley college']
Stanford=['Stanford','stanford']
Endings=[' ','.','?','"',"'",'/','<','!',':',';',"\\"]
Beginnings=['>',' ',',',':',';','.','?','"','!','\\n']
UCLA = addEndings(UCLA,Endings,Beginnings)
USC = addEndings(USC,Endings,Beginnings)
Cal = addEndings(Cal,Endings,Beginnings)
notCal = addEndings(notCal,Endings,Beginnings)
Stanford = addEndings(Stanford,Endings,Beginnings)
f=open('FrequencyData.txt','w')
f.write("Berkeley Stanford UCLA USC")
total=0
for i in x:
	if i[0]:
		total=total+1
		ucla=str(counts(i[0],i[1],UCLA))
		usc=str(counts(i[0],i[1],USC))
		berk=counts(i[0],i[1],Cal)
		berk=str(berk-counts(i[0],i[1],notCal))
		stanford=str(counts(i[0],i[1],Stanford))
		f.write('\n'+berk+' '+stanford+' '+ucla+' '+usc)
f.close()
print (total)
