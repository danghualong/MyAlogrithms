import math

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        costTypes=[1,7,30]
        result=[0 for j in range(len(days)+1)]
        for j in range(1,len(days)+1):
            minCost=result[j-1]+costs[0]
            for i in range(len(costs)):
                if(costTypes[i]>days[j-1]):
                    minCost=min(costs[i],minCost)
                else:
                    # 找到对应的列（此处需要优化)
                    sepK=0
                    for k in range(j):
                        if(days[k-1]<=days[j-1]-costTypes[i]):
                            sepK=k
                    minCost=min(minCost,costs[i]+result[sepK])
            result[j]=minCost
        return result[len(days)]

obj=Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
result=obj.mincostTickets(days,costs)
print(result)