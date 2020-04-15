
import math
from queue import Queue

class Node(object):
    def __init__(self,name):
        self.name=name
        self.adjacent=[]
        self.visited=False
        self.weight=math.inf
    

class StateGraph(object):
    def __init__(self):
        self.vs={}
    def addNode(self,node):
        if(node.name not in self.vs):
            self.vs[node.name]=node
    def addEdge(self,fromNode,toNode):
        self.addNode(fromNode)
        self.addNode(toNode)
        if(toNode.name not in fromNode.adjacent):
            fromNode.adjacent.append(toNode.name)
    def exist(self,node):
        return node.name in self.vs

    def getMiniPath(self,startNodeName,endNodeName):
        startNode=self.vs[startNodeName]
        if(startNodeName==endNodeName):
            print(startNode.weight)
            return
        if(not startNode.visited):
            adjacent=self.vs[startNodeName].adjacent
            nearestNode=None
            weights=math.inf
            for nodeName in adjacent:
                tmpNode=self.vs[nodeName]
                if(not tmpNode.visited):
                    tmpNode.weight=tmpNode.weight if tmpNode.weight<startNode.weight+1 else startNode.weight+1
                    if(weights<tmpNode.weight):
                        weights=tmpNode.weight
                        nearestNode=tmpNode
            if(nearestNode!=None):
                self.getMiniPath(nearestNode.name,endNodeName)
                    
                    
    
size=3

class HuaRongPath(object):
    
    def __init__(self,initNode):
        self.initNode=initNode
    
    def buildGraph(self):
        graph=StateGraph()
        q=Queue()
        tmpNode=self.initNode
        q.put(tmpNode)
        while(q.qsize()>0):
            t=q.get()
            nextNodes=self.getNextNodes(t)
            nonExist=True
            for nextNode in nextNodes:
                if(not graph.exist(nextNode)):
                    nonExist=False
            if(not nonExist):
                for nextNode in nextNodes:
                    q.put(nextNode)
                    graph.addEdge(t,nextNode)
        return graph



    def getNextNodes(self,tmpNode):
        list=[]
        name=tmpNode.name
        index=name.index('0')
        if((index%size)>0):
            namecopy=getSwappedText(name,index,index-1)
            list.append(Node(namecopy))
        if((index%size)<size-1):
            namecopy=getSwappedText(name,index,index+1)
            list.append(Node(namecopy))
        if(int(index/size)>0):
            namecopy=getSwappedText(name,index,index-size)
            list.append(Node(namecopy))
        if(int(index/size)<size-1):
            namecopy=getSwappedText(name,index,index+size)
            list.append(Node(namecopy))
        return list
            

def getSwappedText(str,index1,index2):
    strCopy=list(str)
    tmp=strCopy[index1]
    strCopy[index1]=strCopy[index2]
    strCopy[index2]=tmp
    return ''.join(strCopy)


if __name__=='__main__':
    initNode=Node('012345678')
    obj=HuaRongPath(initNode)
    graph=obj.buildGraph()
    initNode.weight=0
    graph.getMiniPath('012345678','123456780')

        
        
