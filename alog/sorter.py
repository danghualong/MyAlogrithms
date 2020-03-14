class Sorter(object):
    def sort(self,arr,policy):
        policy.sort(arr)

class SortPolicy(object):
    def sort(self,arr):
        pass
    def swap(self,arr,one,other):
        tmp=arr[one]
        arr[one]=arr[other]
        arr[other]=tmp
class BubbleSortPolicy(SortPolicy):
    def sort(self,arr):
        n=len(arr)
        for i in range(n-1,0,-1):
            for j in range(i):
                if(arr[j]>arr[j+1]):
                    self.swap(arr,j,j+1)
class QuickSortPolicy(SortPolicy):
    def sort(self,arr):
        self._quickSort(arr,0,len(arr)-1)

    def _quickSort(self,arr,f,t):
        if(f>=t):
            return
        mid=self._getMid(arr,f,t)
        self._quickSort(arr,f,mid-1)
        self._quickSort(arr,mid+1,t)
            

    def _getMid(self,arr,f,t):
        pos=f
        for i in range(f+1,t+1):
            if(arr[i]<arr[f]):
                pos+=1
                self.swap(arr,i,pos)
        self.swap(arr,f,pos)
        return pos

s=Sorter()
policy=QuickSortPolicy()
arr=[9,5,2,3,4,6,8,1]
s.sort(arr,policy)
print(arr)

        