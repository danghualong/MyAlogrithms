class Solution(object):
    def twoSum(self,nums,target):
        hashNums={}
        for i,num in enumerate(nums):
            nextNum=target-num
            if(nextNum in hashNums):
                return [hashNums[nextNum],i]
            hashNums[num]=i
        return None

    def twoSum2(self,nums,target):
        result=[]
        hashNums={}
        # print(enumerate(nums))
        for i,num in enumerate(nums):
            nextNum=target-num
            if(nextNum in hashNums):
                result.append((hashNums[nextNum],i))
                continue
            else:
                if(num in hashNums):
                    # print(i)
                    continue
                if(nextNum in hashNums):
                    result.append((hashNums[nextNum],i))
            hashNums[num]=i
        return result

s=Solution()
result=s.twoSum2([2,2,3,4,5,7,7,8,9,10,1],4)
print(result)
