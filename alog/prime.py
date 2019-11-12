import math
import numpy as np


def findMax(arr,nFrom,nEnd):
    if(nFrom>=nEnd):
        return arr[nFrom]
    mid=int((nFrom+nEnd)/2)
    max1=findMax(arr,nFrom,mid)
    max2=findMax(arr,mid+1,nEnd)
    return max1 if max1>max2 else max2


arr=[3,2,4,5,7,2,8,4,9,1,0]
m=findMax(arr,0,len(arr)-1)
print(m)
