
def compare(a,b):
    return a<b

def swap(arr,index1,index2):
    minVal=arr[index2]
    arr[index2]=arr[index1]
    arr[index1]=minVal

def buildHeap(arr,startIndex,endIndex):
    sepIndex=int((endIndex-startIndex+1)/2)
    i=sepIndex-1
    while(i>=startIndex):
        minIndex=-1
        if(i*2+2<=endIndex):
            minIndex=i*2+2 if(compare(arr[i*2+1],arr[i*2+2])) else i*2+1
        else:
            minIndex=i*2+1
        if(compare(arr[i],arr[minIndex])):
            swap(arr,i,minIndex)
            tunnel(arr,minIndex,endIndex)
        i-=1

def tunnel(arr,curIndex,endIndex):
    i=curIndex
    while(i<=endIndex):
        minIndex=-1
        if(i*2+2<=endIndex):
            minIndex=i*2+2 if(compare(arr[i*2+1],arr[i*2+2])) else i*2+1
        elif(i*2+1<=endIndex):
            minIndex=i*2+1
        if(minIndex<0):
            break
        if(compare(arr[i],arr[minIndex])):
            swap(arr,i,minIndex)
            i=minIndex
        else:
            break

def sort(arr):
    buildHeap(arr,0,len(arr)-1)
    i=len(arr)-1
    while(i>=1):
        swap(arr,0,i)
        tunnel(arr,0,i-1)
        i-=1

if __name__=='__main__':
    arr=[93,72,48,53,45,30,18,36,15,35]
    print(arr)
    buildHeap(arr,0,len(arr)-1)
    print(arr)
    sort(arr)
    print(arr)
