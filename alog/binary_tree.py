
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    # 构造树
    def createTree(self,nums):
        if(nums==None or len(nums)==0):
            return None
        root=TreeNode(nums[0])
        self._createNode(root,0,nums)
        return root

    def createBalanceTree(self,nums):
        if(nums==None or len(nums)==0):
            return None
        root=self.createBalanceNode(nums,0,len(nums)-1)
        return root
    def createBalanceNode(self,nums,startIndex,endIndex):
        if(startIndex>endIndex):
            return None
        mid=(startIndex+endIndex)//2
        node=TreeNode(nums[mid])
        node.left=self.createBalanceNode(nums,startIndex,mid-1)
        node.right=self.createBalanceNode(nums,mid+1,endIndex)
        return node

    def _createNode(self,parent,index,nums):
        if(parent==None):
            return
        if(index*2+1<len(nums) and nums[index*2+1]!=None):
            node=TreeNode(nums[index*2+1])
            parent.left=node
            self._createNode(node,index*2+1,nums)
        if(index*2+2<len(nums) and nums[index*2+2]!=None):
            node=TreeNode(nums[index*2+2])
            parent.right=node
            self._createNode(node,index*2+2,nums)
    # 获取树的高度
    def getHeight(self,node):
        if(node==None):
            return 0
        h1=self.getHeight(node.left)
        h2=self.getHeight(node.right)
        return 1+max(h1,h2)
    # 可视化树
    def printTree(self,node):
        self._printNode(node,0)

    def _printNode(self,node,level):
        if(node==None):
            return
        print("---"*level,node.val)
        self._printNode(node.left,level+1)
        self._printNode(node.right,level+1)

if __name__ == "__main__":
    tree=BinaryTree()
    root=tree.createBalanceTree([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    tree.printTree(root)
