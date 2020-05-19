# 验证回文字符串，只允许删除一次
class Solution(object):
    def IsPalindromic(self,s):
        return self.rec_test(s,False)


    def rec_test(self,s,deleted):
        if(len(s)<=1):
            return True
        start=0
        stop=len(s)-1
        while(start<stop):
            if(s[start]==s[stop]):
                start+=1
                stop-=1
            else:
                if(deleted):
                    return False
                else:
                    r1=self.rec_test(s[start+1:stop+1],True)
                    r2=self.rec_test(s[start:stop],True)
                    return (r1 or r2)
        return True           
                    

obj=Solution()
t=obj.IsPalindromic("cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu")
print(t)
