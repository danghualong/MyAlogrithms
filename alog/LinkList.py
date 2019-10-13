class Node(object):
    def __init__(self,v):
        self.val=v
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.cursor=None
    
    def add(self,v):
        node=Node(v)
        node.next=self.head
        self.head=node
    
    def length(self):
        count=0
        cur=self.head
        while(cur):
            count+=1
            cur=cur.next
        return count
    
    def remove(self,v):
        cur=self.head
        pre=None
        while(cur!=None):
            if(cur.val==v):
                if(pre):
                    pre.next=cur.next
                else:
                    self.head=cur.next
                return cur
            pre=cur
            cur=cur.next
    
    def append(self,v):
        node=Node(v)
        cur=self.head
        if(cur==None):
            self.head=node
        else:
            while(cur.next):
                cur=cur.next
            cur.next=node

    def pop(self):
        cur=self.head
        if(cur==None):
            return None
        else:
            pre=None
            while(cur.next):
                pre=cur
                cur=cur.next
            if(cur==self.head):
                self.head=None
            else:
                pre.next=None        
            return cur

    def get(self,index):
        if(index<0 or index>=self.length()):
            return None
        else:
            cur=self.head
            i=0
            while(i<index):
                cur=cur.next
                i+=1
            return cur.val

    def __iter__(self):
        return self
    def __next__(self):
        if(self.head):
            if(self.cursor==None):
                self.cursor=self.head
            cursor=self.head
            self.head=self.head.next
            return cursor
        else:
            self.head=self.cursor
            raise StopIteration

    def __str__(self):
        pass


list1=LinkedList()
list1.append(2)
list1.append(4)
list1.append(3)

list2=LinkedList()
list2.append(5)
list2.append(6)
list2.append(4)

len1=list1.length
len2=list2.length
minLen=len2 if len1>len2 else len1

list3=LinkedList()
offset=0
for i in range(minLen):
    a=list1.get(i)
    b=list2.get(i)
    k=a+b+offset
    offset=0
    if(k>=10):
        k=k-10
        offset=1
    list3.append(k)
  




    