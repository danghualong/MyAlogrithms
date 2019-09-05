class Composition(object):
    def __init__(self):
        self._result=[]
        self._indexStack=[]

    def compositionSum(self,arr,target):
        arr.sort()
        len1=len(arr)
        for startIndex in range(len1):
            j=startIndex
            sum=0
            seq=[]
            self._indexStack.clear()
            while(j<len1):
                if(sum+arr[j]<target):
                    seq.append(arr[j])
                    self._indexStack.append(j)
                    sum+=arr[j]
                elif(sum+arr[j]==target):
                    seq.append(arr[j])
                    self._result.append(seq)
                    seq.pop()
                else:
                    lastIndex=self._indexStack.pop()
                    sum-=arr[lastIndex]
                    j=lastIndex
                j+=1

        print(self._result)


arr=[1,2,2,3,4,5]
comp=Composition()
comp.compositionSum(arr,7)
