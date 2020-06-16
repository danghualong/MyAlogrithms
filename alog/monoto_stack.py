
class Solution(object):
    # 单调栈实现最大柱形面积
    def getMaxArea(self,heights):
        stack=[]
        stack.append(-1)
        maxArea=0
        heights.append(-1)
        i=0
        while(i<len(heights)):
            topIndex=stack[len(stack)-1]
            if(heights[i]>=heights[topIndex]):
                stack.append(i)
                i+=1
            else:
                stack.pop()
                area=heights[topIndex]*(i-stack[len(stack)-1]-1)
                if(area>maxArea):
                    maxArea=area
        return maxArea
    # 单调递减栈 实现每日温度
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if(T==None or len(T)==0):
            return None
        
        stack=[]
        stack.append(0)
        results=[0 for i in range(len(T))]
        for i in range(1,len(T)):
            while(len(stack)>0):
                topIndex=stack[len(stack)-1]
                if(T[i]<=T[topIndex]):
                    break
                results[topIndex]=i-topIndex
                stack.pop()
            stack.append(i)
                
        return results


obj=Solution()
print(obj.getMaxArea([2,1,5,6,2,3]))
print(obj.getMaxArea([5,5,4,5,6]))
print(obj.getMaxArea([4,2,0,3,2,5]))

print(obj.dailyTemperatures( [73, 74, 75, 71, 69, 72, 76, 73]))