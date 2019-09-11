class Solution(object):
    def firstMissingPositive(self,arr):
        if(arr==None):
            return
        i=0
        while(i<len(arr)):
            if(arr[i]>0 and arr[i]<=len(arr) and arr[i]!=arr[arr[i]-1]):
                index=arr[i]-1
                tmp=arr[i]
                arr[i]=arr[index]
                arr[index]=tmp
            else:
                i+=1
        for i in range(len(arr)):
            if(arr[i]!=i+1):
                return (i+1)
        return len(arr)+1
    
s=Solution()
missing=s.firstMissingPositive([3,5,2,1])
print(missing)
