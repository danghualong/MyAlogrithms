
class Solution(object):
    def leaps(self,nums):
        if(nums==None or len(nums)<2):
            return 0
        return self.getMinSteps(nums)
    def getMinSteps(self,nums):
        curIndex=0
        count=0
        while(curIndex<len(nums)):
            if(nums[curIndex]+curIndex>=len(nums)-1):
                return count+1
            nextIndex=curIndex+1
            maxV=nums[nextIndex]+nextIndex
            for i in range(1,nums[curIndex]+1):
                if(curIndex+i+nums[curIndex+i]>maxV):
                    maxV=curIndex+i+nums[curIndex+i]
                    nextIndex=curIndex+i
            count+=1
            curIndex=nextIndex
        return count    







nums=[1 for i in range(10000)]
print(Solution().leaps(nums))
    
