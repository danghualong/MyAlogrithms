
from binary_tree import TreeNode

class MyNode(TreeNode):
    def __init__(self,val):
        super(MyNode,self).__init__(val)
        self.leftP=0
        self.rightP=0

class Solution(object):
    def __init__(self):
        self.list=[]

    def getMaxP(self,count):
        root=MyNode("")
        result=[]
        self.createNode(root,count,result)
        return result
    
    def getMaxP_DP(self,count):
        result=[[] for i in range(count+1)]
        result[0]=['']
        for i in range(1,count+1):
            for j in range(i):
                tmpArr1=result[j]
                tmpArr2=result[i-j-1]
                for item1 in tmpArr1:
                    for item2 in tmpArr2:
                        result[i].append('('+item1+')'+item2)
        return result[count]


    def createNode(self,parent,count,result):
        if(parent!=None):
            if(parent.leftP<count):
                left=MyNode(parent.val+"(")
                left.leftP=parent.leftP+1;
                left.rightP=parent.rightP
                parent.left=left
            if(parent.rightP<parent.leftP):
                right=MyNode(parent.val+")")
                right.leftP=parent.leftP
                right.rightP=parent.rightP+1
                parent.right=right
                if(right.rightP==right.leftP and right.rightP==count):
                    result.append(right.val)
            self.createNode(parent.left,count,result)
            self.createNode(parent.right,count,result)


obj=Solution()
n=6
print("动态规划算法：")
result=obj.getMaxP_DP(n)  
print(len(result))
print(result)
print("DFS：")
result=obj.getMaxP(n)  
print(len(result))
print(result)  
