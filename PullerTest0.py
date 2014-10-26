from array import *
def openPage (n):
	pageData = str(urllib.request.urlopen(baseUrl+str(n)).read())
	return pageData
def completionIndex(stream,tags):
	for i in range(0,len(tags)):
		if stream==tags[i]:
			return i
	return -1
def isMatch(char,tags,index):
	for str in tags:
		if index<len(str):
			if char==str[index]:
				return True
	return False
def parseData (data):
	parsed=['','','','','','0']
	tags=['<div class="Message">','class="Permalink" rel="nofollow"><time title="','rel="next','rel="canonical" href="']
	ends=['</div>','"','>','.html']
	scanningIndex=0
	isScanning=False
	isReading=False
	isEnding=False
	endStream=''
	stream=''
	i=0
	firstPost=2
	gotLink=False
	for char in data:
		if isScanning==False and isReading==False:
			if isMatch(char,tags,scanningIndex):
				isScanning=True
				scanningIndex=scanningIndex+1
				stream = stream + char
		elif isScanning==True:
			if isMatch(char,tags,scanningIndex):
				scanningIndex=scanningIndex+1
				stream = stream + char
			elif scanningIndex>8:
				i = completionIndex(stream,tags)
				#print(i)
				if i==-1:
					scanningIndex=0
					isScanning=False
					stream=''
				else:
					isScanning=False
					isReading=True
					stream=char
					scanningIndex=0
					if i==2:
						if gotLink:
							isReading=False
							stream=''
						else:
							gotLink=True
			else:
				scanningIndex=0
				isScanning=False
				stream=''
		elif isReading==True:
			if isEnding:
				if endStream==ends[i]:
					isReading=False
					scanningIndex=0
					isScanning=False
					isEnding=False
					if i==0:
						parsed[5]=str(int(parsed[5])+1)
					if firstPost==0:
						parsed[0]=stream
						firstPost=firstPost-1
					else:
						parsed[i+1]=parsed[i+1]+stream
						firstPost=firstPost-1
					stream=''
					endStream=''
				elif char==ends[i][scanningIndex]:
					endStream=endStream+char
					scanningIndex=scanningIndex+1
				else:
					isEnding=False
					scanningIndex=0
					stream=stream+endStream+char
					endStream=''
			else:
				if char==ends[i][scanningIndex]:
					isEnding=True
					endStream=endStream+char
					scanningIndex=scanningIndex+1
				else:
					stream=stream+char
	if len(parsed[3])>0:
		new=parseNextPage(parsed[4],2)
		parsed[1]=parsed[1]+new[0]
		parsed[5]=str(int(parsed[5])+int(new[2]))
	return [parsed[0],parsed[1],parsed[2],parsed[5]]




def parseNextPage(base,number):
	nextUrl=(base+'-p'+str(number)+'.html')
	#print(nextUrl)
	nextData=str((urllib.request.urlopen(nextUrl).read()))
	parsed=['','','0']
	tags=['<div class="Message">','rel="next',]
	ends=['</div>','>',]
	scanningIndex=0
	isScanning=False
	isReading=False
	isEnding=False
	endStream=''
	stream=''
	i=0
	gotLink=False
	for char in nextData:
		if isScanning==False and isReading==False:
			if isMatch(char,tags,scanningIndex):
				isScanning=True
				scanningIndex=scanningIndex+1
				stream = stream + char
		elif isScanning==True:
			if isMatch(char,tags,scanningIndex):
				scanningIndex=scanningIndex+1
				stream = stream + char
			elif scanningIndex>8:
				i = completionIndex(stream,tags)
				#print(i)
				if i==-1:
					scanningIndex=0
					isScanning=False
					stream=''
				else:
					isScanning=False
					isReading=True
					stream=char
					scanningIndex=0
					if i==2:
						if gotLink:
							isReading=False
							stream=''
						else:
							gotLink=True
			else:
				scanningIndex=0
				isScanning=False
				stream=''
		elif isReading==True:
			if isEnding:
				if endStream==ends[i]:
					isReading=False
					scanningIndex=0
					isScanning=False
					isEnding=False
					parsed[i]=parsed[i]+stream
					if i==0:
						parsed[2]=str(int(parsed[2])+1)
					stream=''
					endStream=''
				elif char==ends[i][scanningIndex]:
					endStream=endStream+char
					scanningIndex=scanningIndex+1
				else:
					isEnding=False
					scanningIndex=0
					stream=stream+endStream+char
					endStream=''
			else:
				if char==ends[i][scanningIndex]:
					isEnding=True
					endStream=endStream+char
					scanningIndex=scanningIndex+1
				else:
					stream=stream+char
	if len(parsed[1])>0:
		new=parseNextPage(base,number+1)
		parsed[0]=parsed[0]+new[0]
		parsed[2]=str(int(parsed[2])+int(new[2]))
	return parsed





			
				



import urllib.request
import time
import random
import pickle
t1=time.time()
baseUrl = 'http://talk.collegeconfidential.com/discussion/'
data=[]
srs=random.sample(range(26,1600000),15000)
index=0
n=10000
badLinks=0
f=open("testData.txt",'wb')
while n>0:
	try:
		print(10001-n)
		data.append(parseData(openPage(srs[index])))
		index=index+1
		n=n-1
	except:
		print("except")
		print(srs[index])
		badLinks=badLinks+1
		index=index+1
pickle.dump(data,f)
f.close()
print(time.time()-t1)
print(badLinks)

