arr= []
indexArr=[]
arrRecur = []
indexArrRecur=[]

events = [[8,11],[6,10],[5,9],[3,9],[12,16],[2,14],[8,12],[5,7],[0,6],[3,5],[1,4]]

def sortEvents():   
	for i in range(1,len(events)):
		key = events[i]
		j=i-1
		while(j>=0 and key[1]<events[j][1]):
			events[j+1]=events[j]
			j-=1
		events[j+1] = key


def ActivitySelection(testEvent,x):
	arr.append(testEvent[x])
	indexArr.append(x)
	currEvent = arr[len(arr)-1]
	for k in range(1,len(testEvent)):
		if(currEvent[1]<=testEvent[k][0]):
			arr.append(testEvent[k])
			indexArr.append(k)
			currEvent = arr[len(arr)-1]   
	return(indexArr)

def ActivitySelectionRecursive(testEvent,startIndex,currIndex,totalLen):
	if(currIndex<totalLen):
		if(startIndex == currIndex):      
			arrRecur.append(testEvent[currIndex])
			indexArrRecur.append(currIndex)
			currIndex+=1
			return ActivitySelectionRecursive(testEvent,startIndex,currIndex,totalLen)
		else:								
			tempIndex =len(arrRecur)-1
			if(arrRecur[tempIndex][1]<=testEvent[currIndex][0]):
				arrRecur.append(testEvent[currIndex])
				indexArrRecur.append(currIndex)
			currIndex+=1
			return ActivitySelectionRecursive(testEvent,startIndex,currIndex,totalLen)
	else:
		return indexArrRecur



if __name__=="__main__":
	sortEvents()
	print(events)
	x=input("From the above events select index for which to find successive feasible events:")
	print("From Iterative Model")
	print(ActivitySelection(events,int(x)))
	print("From Recursive Model")
	print(ActivitySelectionRecursive(events,int(x),int(x),len(events)))

