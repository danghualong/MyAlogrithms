class Solution(object):
    def calc(self,nums):
        if(nums==None or len(nums)==0):
            return None
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(0,n-2):
            if(i>0 and curNum==nums[i]):
                continue
            curNum=nums[i]
            left=i+1
            right=n-1
            while(left<right):
                total=curNum+nums[left]+nums[right]
                if(total==0):
                    result.append([curNum,nums[left],nums[right]])
                    left+=1
                    while(left<right and nums[left-1]==nums[left]):
                        left+=1
                    right-=1
                    while(left<right and nums[right]==nums[right+1]):
                        right-=1
                elif(total<0):
                    left+=1
                    while(left<right and nums[left-1]==nums[left]):
                        left+=1
                else:
                    right-=1
                    while(left<right and nums[right]==nums[right+1]):
                        right-=1
        return result

obj=Solution()
nums = [-2, 0, 0, 2, 2]
result=obj.calc(nums)
print(result)                