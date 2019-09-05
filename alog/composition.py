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
                    if(j==len1-1):
                        if(len(seq)>0):
                            j=self._indexStack.pop()
                            seq.pop()
                            sum-=arr[j]
                    else:
                        seq.append(arr[j])
                        self._indexStack.append(j)
                        sum+=arr[j]
                elif(sum+arr[j]==target):
                    seq.append(arr[j])
                    self._result.append(seq[:])
                    seq.pop()
                    if(j==len1-1):
                        if(len(seq)>0):
                            j=self._indexStack.pop()
                            seq.pop()
                            sum-=arr[j]
                else:
                    # print(seq,arr[j])
                    j=self._indexStack.pop()
                    seq.pop()
                    sum-=arr[j]
                    
                if(len(seq)==0):
                    # print("---"+str(startIndex)+"-----")
                    break
                # print("----",self._result)
                j+=1

        print(self._result)


arr=[1,6,2,3,4,5]
comp=Composition()
comp.compositionSum(arr,12)
