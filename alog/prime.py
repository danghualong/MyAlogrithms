import math


def findMax(arr,nFrom,nEnd):
    if(nFrom>=nEnd):
        return arr[nFrom]
    mid=int((nFrom+nEnd)/2)
    max1=findMax(arr,nFrom,mid)
    max2=findMax(arr,mid+1,nEnd)
    return max1 if max1>max2 else max2


arr=[3,2,4,5,7,2,8,4,9,1,0]
# m=findMax(arr,0,len(arr)-1)
# print(m)

def hailSuppose(n):
    times=0
    m=n
    while(n>1):
        if(n%2==0):
            n=n/2
        else:
            n=n*3+1
        times+=1
    print('{0}:{1}'.format(m,times))

for i in range(2,100):
    hailSuppose(i)
