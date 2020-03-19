# �Ӽ������ҳ���������2�����ĺ�Ϊָ��Ŀ��ֵ
class Solution(object):
    # �Ӽ������ҳ�һ������2�����ĺ͵���Ŀ��ֵ
    def find_one(self,nums,target):
        hashNums={}
        for i,num in enumerate(nums):
            nextNum=target-num
            if(nextNum in hashNums):
                return [hashNums[nextNum],i]
            hashNums[num]=i
        return None
    # �Ӽ������ҳ���������2�����ĺ͵���Ŀ��ֵ
    def find_composition(self,nums,target):
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
result=s.find_composition([2,2,3,4,5,7,7,8,9,10,1],4)
print(result)
print(result)