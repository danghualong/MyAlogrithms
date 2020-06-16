# 前面块的最大值不能高于后面块的最小值
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if(arr==None or len(arr)==0):
            return 0
        i=0
        blocks=0
        while(i<len(arr)):
            nextIndex=i
            for j in range(i+1,len(arr)):
                if(arr[i]>arr[j]):
                    nextIndex=j
            maxIndex=i
            maxV=arr[i]
            for j in range(i+1,nextIndex):
                if(maxV<arr[j]):
                    maxV=arr[j]
                    maxIndex=j
            if(maxIndex!=i):
                i=maxIndex
            else:
                i=nextIndex+1
                blocks+=1
        return blocks

    def maxChunksToSorted2(self,arr):
        if (len(arr)== 0):
            return 0
        mins = [0 for i in range(len(arr))]
        mins[len(arr)- 1] = arr[len(arr) - 1]
        for i in range(len(arr) - 2,-1,-1):
            mins[i] = min(arr[i], mins[i + 1])
        print(mins)
        count = 1
        pre = arr[0]
        for i in range(1,len(arr)):
            if (pre > mins[i]):
                if (arr[i] > pre):
                    pre = arr[i]
            else:
                count+=1
                pre = arr[i]
        return count

    def maxChunksToSorted3(self,arr):
        n=len(arr)
        prefix_max=[0 for i in range(n)]
        suffix_min=[0 for i in range(n)]
        prefix_max[0]=arr[0]
        for i in range(1,n):
            prefix_max[i]=max(prefix_max[i-1],arr[i])
        suffix_min[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            suffix_min[i]=min(suffix_min[i+1],arr[i])
        count=1
        for i in range(n-1):
            # 前缀最大小于后缀最小
            if (prefix_max[i]<=suffix_min[i+1]):
                count+=1
        return count

obj=Solution()
print(obj.maxChunksToSorted([1,4,0,2,3,5]))
print(obj.maxChunksToSorted2([1,4,0,2,3,5]))
print(obj.maxChunksToSorted3([1,4,0,2,3,5]))

print(obj.maxChunksToSorted2([1,0,4,2,3,5]))
print(obj.maxChunksToSorted3([1,0,4,2,3,5]))
