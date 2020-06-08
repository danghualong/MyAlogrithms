class Node(object):
    def __init__(self,key):
        self.next=None
        self.prev=None
        self.key=key
# 并查集类
class MergeFindSet(object):
    def __init__(self,items):
        self.dict={}
        if(items!=None):
            for item in items:
                if(item not in self.dict):
                    self.dict[item]=Node(item)  
    def union(self,relatives):
        if(relatives==None):
            return
        for item in relatives:
            if(item not in self.dict):
                return False
        item0=relatives[0]
        curTail=self._getTail(self.dict[item0])
        for i in range(1,len(relatives)):
            item=relatives[i]
            if(self.isSameSet(item0,item)):
                continue
            curNode=self.dict[item]
            curHeader=self._getHead(curNode)
            curTail.next=curHeader
            curHeader.prev=curTail
            curTail=self._getTail(curHeader)

    def isSameSet(self,a,b):
        if(a==None or b==None):
            return False
        if(a not in self.dict or b not in self.dict):
            return False
        headerA=self._getHead(self.dict[a])
        headerB=self._getHead(self.dict[b])
        return headerA==headerB

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

# 利用并查集查找变量赋值是否有冲突
class Solution(object):
    def equationsPossible(self, equations):
        if(equations==None or len(equations)<=0):
            return True
        n=len(equations)
        items=[None for i in range(n)]
        start=0
        stop=n-1
        letters=set()
        for item in equations:
            if('==' in item):
                items[start]=item
                arr=item.split('==')
                letters.update(arr)
                start+=1
            else:
                items[stop]=item
                arr=item.split('!=')
                letters.update(arr)
                stop-=1
        obj=MergeFindSet(letters)
        for item in items:
            if('==' in item):
                arr=item.split('==')
                obj.union(arr)
            else:
                arr=item.split('!=')
                if(obj.isSameSet(arr[0],arr[1])):
                    return False
        return True


obj=Solution()
result=obj.equationsPossible(["c==c","b==d","x!=z"])
print(result)


