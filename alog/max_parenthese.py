
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
        print(result)

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
obj.getMaxP(10)       
