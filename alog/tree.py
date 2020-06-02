from binary_tree import BinaryTree

class Solution(object):
    def __init__(self,treeBuilder):
        self.treeBuilder=treeBuilder
    # 修剪BST
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        cur=root
        print("before cut:")
        self.treeBuilder.printTree(root)
        self.getTrimmedParent(cur,L,R)
        print("After Cut:")
        self.treeBuilder.printTree(root)
    
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

    def isSymmetric(self, root):
        if(root==None):
            return True
        return self._isChildSymmetric(root.left,root.right)

    def _isChildSymmetric(self,leftNode,rightNode):
        if(leftNode==None and rightNode==None):
            return True
        if(leftNode!=None and rightNode!=None):
            if(leftNode.val==rightNode.val):
                t1=self._isChildSymmetric(leftNode.left,rightNode.right)
                t2=self._isChildSymmetric(leftNode.right,rightNode.left)
                return t1 and t2
        return False 


builder=BinaryTree()
obj=Solution(builder)
nums=[3,0,4,None,2,None,None,None,None,1]   
root=builder.createTree(nums)
obj.trimBST(root,1,3)

nums=[1,2,2,3,4,4,3]
root=builder.createTree(nums)
print(obj.isSymmetric(root))



         
             