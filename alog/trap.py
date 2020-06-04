# 计算区间总蓄水量
class Solution(object):
    def trap(self,height):
        if(height==None or len(height)<3):
            return 0
        stack=[0]
        maxHeight=height[0]
        maxIndex=0
        i=1
        # 先找出可能蓄水的区间
        while(i<len(height)):
            if(height[i]<height[stack[len(stack)-1]]):
                stack.append(i)
            else:
                while(len(stack)>0):
                    # 当当前高度小于栈内的高度
                    if(height[stack[len(stack)-1]]>height[i]):
                        break
                    if(stack[len(stack)-1]==maxIndex):
                        break
                    stack.pop()
                stack.append(i)
                if(height[i]>maxHeight):
                    maxHeight=height[i]
                    maxIndex=i
            i+=1
        # 计算总蓄水量
        vol=0
        for i in range(len(stack)-1,0,-1):
            right=height[stack[i]]
            left=height[stack[i-1]]
            width=stack[i]-stack[i-1]-1
            minHeight=min(left,right)
            tmpSum=0
            for j in range(stack[i-1]+1,stack[i]):
                tmpSum+=height[j]
            # 对于那些单调的区间，不能蓄水
            if(width*minHeight<tmpSum):
                continue
            vol+=(width*minHeight-tmpSum)
        return vol
        



            

                    
obj=Solution()
heights=[0,1,0,2,1,0,1,3,2,1,2,1]
obj.trap(heights)                
