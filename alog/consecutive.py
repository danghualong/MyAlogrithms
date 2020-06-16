
# 最长的连续子序列
class Solution(object):
    def longestConsecutive(self,nums):
        dict={}
        for i in range(len(nums)):
            if(nums[i] not in dict):
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
        longest=0 if len(nums)==0 else 1
        for i in range(len(nums)):
            add=1
            if(nums[i]-1 in dict):
                # curNum=nums[i]
                # while(curNum-1 in dict):
                #     add+=1
                #     dict.pop(curNum-1)
                #     if(add>longest):
                #         longest=add
                #     curNum-=1
                continue
            if(nums[i]+1 in dict):
                curNum=nums[i]
                while(curNum+1 in dict):
                    add+=1
                    dict.pop(curNum+1)
                    if(add>longest):
                        longest=add
                    curNum+=1 
        return longest
               



                


 
obj=Solution()
result=obj.longestConsecutive([3,4,6,2,9,8,7])
print(result)
