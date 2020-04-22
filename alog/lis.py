# 寻找最长递增子序列(nlogn时间复杂度)
import math
class LISSearcher(object):
    def __init__(self,arr):
        self.arr=arr

    def _binSearch(self,seqList,c,start,end):
        """二分查找,返回要更新的元素索引        
        Arguments:
            seqList -- [对应的数据结构[t,count,index]]
        Returns:
            元素索引，当为-1时，表示不需要更新该集合
        """          
        if(start>end):
            return start
        mid=int((start+end)/2)
        data=seqList[mid][0]
        if(data==c):
            return -1
        elif(data>c):
            return self._binSearch(seqList,c,start,mid-1)
        else:
            return self._binSearch(seqList,c,mid+1,end)

    def _getSeq(self,seqList):
        """获取最长递增子序列
        
        Arguments:
            seqList -- [对应的数据结构[t,count,index]]
        
        Returns:
            [type] -- [description]
        """        
        seq=[]
        endIndex=seqList[len(seqList)-1][2]
        for i in range(endIndex,-1,-1):
            if(len(seq)==0 or seq[len(seq)-1]>self.arr[i]):
                seq.append(self.arr[i])
        return seq[::-1]

    def search(self):
        if(self.arr==None or len(self.arr)<=0):
            return None
        seqList=[]
        seqList.append([self.arr[0],1,0])
        for i in range(1,len(self.arr),1):
            lastElement=seqList[len(seqList)-1]
            # 如果当前元素大于seqList的最后一个元素，直接将该元素添加
            # 至seqList
            if(self.arr[i]>lastElement[0]):
                seqList.append([self.arr[i],lastElement[1]+1,i])
            else:
                t=self._binSearch(seqList,self.arr[i],0,len(seqList)-1)
                # 当t==-1时，表示不需要更新该seqList
                if(t>=0):
                    seqList[t][0]=self.arr[i]
                    seqList[t][2]=i
        return self._getSeq(seqList)


if __name__=='__main__':
    txt='announceytf'
    searcher=LISSearcher(list(txt))
    seq=searcher.search()
    print(seq)
