class Solution(object):
    # 用递归的方法计算石子总数差异
    def stoneII2(self,piles):
        dis=self.diff(piles,0,1)
        return dis
        
    def diff(self,piles,startIndex,maxStep):
        if(startIndex>len(piles)-1):
            return 0
        maxDis=-1e5
        for i in range(1,2*maxStep+1):
            maxDis=max(maxDis,sum(piles[startIndex:startIndex+i])-self.diff(piles,startIndex+i,max(i,maxStep)))
        return maxDis

    def stoneII_DP(self,piles):
        pass

obj=Solution()
piles=[2,7,9,4,4]
print(obj.stoneII2(piles))

