class Solution(object):
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


obj=Solution()
print(obj.getMaxArea([2,1,5,6,2,3]))
print(obj.getMaxArea([5,5,4,5,6]))
print(obj.getMaxArea([4,2,0,3,2,5]))