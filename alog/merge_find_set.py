class Node(object):
    def __init__(self,key,size):
        self.next=None
        self.prev=None
        self.key=key
        self.size=size

class MergeFindSet(object):
    def __init__(self):
        self.dict={}
        
    def merge(self,relatives):
        if(relatives==None):
            return
        curTail=None
        for item in relatives:
            if(item not in self.dict):
                self.dict[item]=Node(item)
            curNode=self.dict[item]
            if(curTail==None):
                curTail=self._getTail(curNode)
            else:
                curHeader=self._getHead(curNode)
                curTail.next=curHeader
                curHeader.prev=curTail
                curTail=self._getTail(curTail)

    def isSameSet(self,items):
        if(items==None):
            return False
        if(items[0] not in self.dict):
            return False
        header=self._getHead(self.dict[items[0]])
        for i in range(1,len(items)):
            if(items[i] not in self.dict):
                return False
            tmpHeader=self._getHead(self.dict[items[i]])
            if(header!=tmpHeader):
                return False
        return True

    def _getTail(self,node):
        if(node==None):
            return None
        tmp=node
        while(True):
            if(tmp.next==None):
                return tmp
            tmp=tmp.next

    def _getHead(self,node):
        if(node==None):
            return None
        tmp=node
        while(True):
            if(tmp.prev==None):
                return tmp
            tmp=tmp.prev

    def getSetSize(self):
        size=0
        for key in self.dict:
            if(self.dict[key]!=None and self.dict[key].prev==None):
                self.printList(self.dict[key])
                size+=1
        return size

    def printList(self,node):
        str=''
        while(node!=None):
            str+=(node.key+"-->")
            node=node.next
        print(str)
        

obj=MergeFindSet()
obj.merge(['Jim','Jimmy'])
obj.merge(['LiLei','WangJun'])
obj.merge(['WangJun','Jimmy'])
obj.merge(['LiMei','LiYing'])
obj.merge(['LiuYing','XiaoCui'])
obj.merge(['XiaoCui','XiangXiu'])
obj.merge(['Dajiao'])
obj.merge(['LiuYing','LiYing'])
print(obj.getSetSize())

