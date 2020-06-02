# 递归实现排列算法
class Solution(object):
    def __init__(self):
        self.result=[]
    # 全排列算法
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(nums==None):
            return None
        if(len(nums)==1):
            return [[nums[0]]]
        else:
            result=[]
            for i in range(len(nums)):
                sub=nums[0:i]+nums[i+1:]
                list=self.permute(sub)
                for item in list:
                    item.insert(0,nums[i])
                    result.append(item)
            return result
    #全排列去重
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(nums==None):
            return None
        if(len(nums)==1):
            return [[nums[0]]]
        else:
            result=[]
            existdNums=[]
            for i in range(len(nums)):
                # 元素如果参与排列,则不参与排列
                if(nums[i] in existdNums):
                    continue
                existdNums.append(nums[i])
                sub=nums[0:i]+nums[i+1:]
                list=self.permuteUnique(sub)
                for item in list:
                    item.insert(0,nums[i])
                    result.append(item)
            return result

    def permute2(self,nums):
        if(nums==None):
            return None
        self.backtrack('',nums,0)
        return self.result

    def backtrack(self,item,nums,i):
        if(i==len(nums)):
            self.result.append(item)
        else:
            for t in range(len(item)+1):
                self.backtrack(item[:t]+str(nums[i])+item[t:],nums,i+1)


o=Solution()
items=o.permute([1,2,3,4])
print(items)

print("\n")
items2=o.permuteUnique([1,2,1,4])
print(items2)

print("\n")
items=o.permute2([1,2,3,4])
print(items)
            