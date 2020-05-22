
class TreeNode(object):
    def __init__(self,x):
        self.x=x
        self.left=None
        self.right=None
    
class Solution(object):
    def __init__(self):
        self.root=None
    
    def buildTree(self, preorder, inorder):
        if(preorder==None or inorder==None):
            return None
        if(len(preorder)==0 or len(inorder)==0):
            return None
        self.buildSubTree(self.root,preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
        return self.root

    
    def buildSubTree(self,parent,preorder,pstart,pstop,inorder,istart,istop,nodeType=0):
        # print(pstart,pstop,istart,istop)
        if(pstart>pstop):
            return
        data=preorder[pstart]
        node=TreeNode(data)
        if(nodeType==1):
            parent.left=node
        elif(nodeType==2):
            parent.right=node
        else:
            self.root=node
        index=inorder.index(data)
        self.buildSubTree(node,preorder,pstart+1,pstart+index-istart,inorder,istart,index-1,1)
        self.buildSubTree(node,preorder,pstart+index-istart+1,pstop,inorder,index+1,istop,2)

    def printTree(self,cur):
        if(cur!=None):
            print(cur.x)
            self.printTree(cur.left)
            self.printTree(cur.right)

preorder=['a','b','d','c','e']
inorder=['b','d','a','e','c']
obj=Solution()
result=obj.buildTree(preorder,inorder)
obj.printTree(obj.root)