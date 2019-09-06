class Composition(object):
    def combinationSum2(self,arr,target):
        arr.sort()
        len1=len(arr)
        result=[]
        indexStack=[]
        seq=[]
        j=0
        sum=0
        canback=False
        while(j<len1):
            if(sum+arr[j]<=target):
                seq.append(arr[j])
                indexStack.append(j)
                sum+=arr[j]
                canback=(j==len1-1)
                if(sum==target):
                    self.addSeq(result,seq)
                    canback=True
            else:
                canback=True

            while(canback and len(seq)>0):
                #如果是最后一个元素，
                j=indexStack.pop()
                seq.pop()
                sum-=arr[j]
                if(j<len1-1): 
                    break
            j+=1
        return result
    
    @staticmethod
    def addSeq(result,seq):
        for tmpSeq in result:
            if(Composition.isSame(tmpSeq,seq)):
                return
        result.append(seq[:])

    @staticmethod       
    def isSame(tmpSeq,seq):
        if(len(tmpSeq)!=len(seq)):
            return False
        for i in range(len(seq)):
            if(tmpSeq[i]!=seq[i]):
                return False
        return True       


arr=[4,4,2,1,4,2,2,1,3]
comp=Composition()
print(comp.combinationSum2(arr,6))
