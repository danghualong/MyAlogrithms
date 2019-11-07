#encoding=utf-8

class QuickSorter(object):
    def __init__(self,list):
        self._list=list

    def getList(self):
        return self._list

    def sort(self,start,end):
        if(start>=end):
            return
        mid=self.split(start,end)
        self.sort(start,mid-1)
        self.sort(mid+1,end)

    def split(self,start,end):
        pivot=self._list[start]
        cursor=start+1
        for i in range(start+1,end+1):
            if(self._list[i]<=pivot):
                #swap the element
                self.swap(i,cursor)
                cursor+=1
        self.swap(start,cursor-1)
        return cursor-1
                 
                
    def swap(self,i,j):
        tmp=self._list[i]
        self._list[i]=self._list[j]
        self._list[j]=tmp


if __name__=="__main__":
    arr=[5,3,7,4,6,5,2,7]
    sorter=QuickSorter(arr)
    sorter.sort(0,len(arr)-1)
    print(sorter.getList())