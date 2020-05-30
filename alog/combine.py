class Solution(object):
    def combine(self,nums):
        return self.combine_sub(nums,0)
    
    def combine_sub(self,letters,startIndex):
        if(startIndex==len(letters)-1):
            return [[],[letters[startIndex]]]
        result=self.combine_sub(letters,startIndex+1)
        copiedResult=[]
        for item in result:
            print(item.copy())
            copiedResult.append(item.copy())
        for item in copiedResult:
            item.insert(0,letters[startIndex])
            result.append(item)
        return result

obj=Solution()
letters=[1,2,3,4,5]
print(obj.combine(letters))


            