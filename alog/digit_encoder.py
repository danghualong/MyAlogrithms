class Solution(object):
    # 动态规划求解编码数量
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num==None):
            return 0
        txt=str(num)
        nums=[0 for i in range(len(txt))]
        for i in range(len(txt)):
            if(i==0):
                nums[0]=1
                continue
            t=int(txt[i-1:i+1])
            if(i==1):
                if(t<26 and t>=10):
                    nums[i]=2
                else:
                    nums[i]=1
                continue
            if(t<26 and t>=10):
                nums[i]=nums[i-1]+nums[i-2] 
            else:
                nums[i]=nums[i-1] 
        print(nums)  
        return nums[len(nums)-1]

obj=Solution()
print(obj.translateNum(25012))