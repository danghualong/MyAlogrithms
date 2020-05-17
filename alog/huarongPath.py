
import math
# BFS算法查找所有可能的状态，并添加到以指定状态为根节点的树中
class Node(object):
    def __init__(self,name):
        self.name=name
        self.level=-1
        self.adjacent=[]
        self.parent=None

class HuaRongPath(object):
    def __init__(self,initNodeName,stopNodeName):
        self.initNodeName=initNodeName
        self.stopNodeName=stopNodeName
        self.size=int(math.sqrt(len(initNodeName)))
        self.root=None
        self.nodes={}
    
    def buildTree(self):
        initNode=Node(self.initNodeName)
        initNode.level=0
        self.root=initNode
        self.nodes[self.initNodeName]=initNode
        self._build()

    def _build(self):
        q=[]
        q.insert(0,self.root)
        while(len(q)>0):
            curNode=q.pop()
            childNodeNames=self.getNextNodes(curNode)
            for tmpName in childNodeNames:
                # 剪枝处理
                if(tmpName not in self.nodes):
                    tmpNode=Node(tmpName)
                    curNode.adjacent.append(tmpNode)
                    tmpNode.parent=curNode
                    tmpNode.level=curNode.level+1
                    self.nodes[tmpName]=tmpNode
                    q.insert(0,tmpNode)
                    # 发现终节点结束操作
                    if(tmpName==self.stopNodeName):
                        return

    def getPaths(self):
        if(self.stopNodeName not in self.nodes):
            print("no path")
            return None
        paths=[]
        curNode=self.nodes[self.stopNodeName]
        paths.append(self.stopNodeName)
        while(curNode.name!=self.initNodeName):
            curNode=curNode.parent
            paths.append(curNode.name)
        return paths[::-1]

    def getNextNodes(self,tmpNode):
        list=[]
        size=self.size
        name=tmpNode.name
        index=name.index('0')
        if((index%size)>0):
            namecopy=getSwappedText(name,index,index-1)
            list.append(namecopy)
        if((index%size)<size-1):
            namecopy=getSwappedText(name,index,index+1)
            list.append(namecopy)
        if(int(index/size)>0):
            namecopy=getSwappedText(name,index,index-size)
            list.append(namecopy)
        if(int(index/size)<size-1):
            namecopy=getSwappedText(name,index,index+size)
            list.append(namecopy)
        return list
            

def getSwappedText(str,index1,index2):
    strCopy=list(str)
    tmp=strCopy[index1]
    strCopy[index1]=strCopy[index2]
    strCopy[index2]=tmp
    return ''.join(strCopy)

def printPaths(paths):
    for path in paths:
        size=int(math.sqrt(len(path)))
        strPath=list(path)
        print('--------------')
        for i in range(size):
            print(strPath[i*size:(i+1)*size])

if __name__=='__main__':
    obj=HuaRongPath('123405678','123456780')
    obj.buildTree()
    paths=obj.getPaths()
    if(paths!=None):
        print(paths)
        printPaths(paths)
