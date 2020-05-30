class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class TreeBuilder(object):
    
    def createTree(self,nums):
        if(nums==None or len(nums)==0):
            return None
        root=TreeNode(nums[0])
        self.createNode(root,0,nums)
        return root

    def createNode(self,parent,index,nums):
        if(parent==None):
            return
        if(index*2+1<len(nums) and nums[index*2+1]!=None):
            node=TreeNode(nums[index*2+1])
            parent.left=node
            self.createNode(node,index*2+1,nums)
        if(index*2+2<len(nums) and nums[index*2+2]!=None):
            node=TreeNode(nums[index*2+2])
            parent.right=node
            self.createNode(node,index*2+2,nums)


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        cur=root
        print("before cut:")
        self.printTree(root,0)
        self.getTrimmedParent(cur,L,R)
        print("After Cut:")
        self.printTree(root,0)
    
    # 获取经过修剪的当前节点
    def getTrimmedParent(self,node,L,R):
        if(node==None):
           return node
        if(node.val<L):
            return self.getTrimmedParent(node.right,L,R)
        if(node.val>R):
            return self.getTrimmedParent(node.left,L,R)
        node.left=self.getTrimmedParent(node.left,L,R)
        node.right=self.getTrimmedParent(node.right,L,R)
        return node 

    def printTree(self,node,index):
        if(node==None):
            return
        print('=='*index,node.val)
        self.printTree(node.left,index+1)
        self.printTree(node.right,index+1)

obj=Solution()
builder=TreeBuilder()
nums=[3,0,4,None,2,None,None,None,None,1]   
root=builder.createTree(nums)
obj.trimBST(root,1,3)



         
             