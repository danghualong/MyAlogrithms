# 构造huffman树

class Node(object):
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
        self.left=None
        self.right=None
        self.code=''
    
    def __str__(self):
        return '{0}:{1}'.format(self.name,self.code)

class Huffman(object):
    def __init__(self,nodes):
        self.root=None
        self.nodes=nodes.copy()
        self._buildTree()

    def _buildTree(self):
        tmpNodes=self.nodes.copy()
        while(len(tmpNodes)>1):
            self._aggregate(tmpNodes)
        self.root=tmpNodes[0]
        self._encodeNode(self.root)



    def _aggregate(self,nodes):
        nodes.sort(key=lambda x:x.weight)
        left=nodes[0]
        right=nodes[1]
        parent=Node("",left.weight+right.weight)
        parent.left=left
        parent.right=right
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(parent)

    def _encodeNode(self,node):
        if(node==None):
            return
        if(node.left is not None):
            node.left.code=node.code+'0'
            node.right.code=node.code+'1'
            self._encodeNode(node.left)
            self._encodeNode(node.right)
        else:
            curNode=[x for x in self.nodes if x.name==node.name]
            curNode[0].code=node.code

    def display(self):
        for node in self.nodes:
            print(node)

if __name__=="__main__":
    nodes=[]
    nodes.append(Node('A',5))
    nodes.append(Node('B',29))
    nodes.append(Node('C',7))
    nodes.append(Node('D',8))
    nodes.append(Node('E',14))
    nodes.append(Node('F',23))
    nodes.append(Node('G',3))
    nodes.append(Node('H',11)) 

    tree=Huffman(nodes)
    tree.display() 

        
            
        
