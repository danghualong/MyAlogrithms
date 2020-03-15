# 递归实现排列算法
class Solution(object):
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


o=Solution()
# items=o.permute([1,2,3,4])
# print(items)

items2=o.permuteUnique([1,2,1,4])
print(items2)
            