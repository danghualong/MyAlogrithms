# 递归和循环算法实现组合算法

class Composition(object):
    #利用数组中的数，每个值可以使用多次，只要加和等于目标值即可
    def combinationSum(self,arr,target):
        arr.sort()
        seq=[]
        result=[]
        i=0
        self.combine(arr,target,i,seq,result)
        return result

    def combine(self,arr,target,start,seq,result):
        if(target==0):
            self.addSeq(result,seq)
            return
        for i in range(start,len(arr)):
            if(arr[i]<=target):
                seq.append(arr[i])
                # 减而治之的递归算法
                self.combine(arr,target-arr[i],i+1,seq,result)
                seq.pop()

    @staticmethod
    def addSeq(result,seq):
        # for tmpSeq in result:
        #     if(Composition.isSame(tmpSeq,seq)):
        #         return
        result.append(seq[:])

    @staticmethod       
    def isSame(tmpSeq,seq):
        if(len(tmpSeq)!=len(seq)):
            return False
        for i in range(len(seq)):
            if(tmpSeq[i]!=seq[i]):
                return False
        return True  
    #从数组中算出所有加和等于目标值的子序列集合(循环实现)
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
    #从数组中算出所有加和等于目标值的子序列集合(递归实现)
    def compose(self,arr,target):
        seq=[]
        index=0
        self.backtrack(arr,target,seq,index)

    def backtrack(self,arr,target,seq,index):
        if(target==0):
            return
        if(index>=len(arr)):
            return
        if(target>=arr[index]):
            seq.append(arr[index])
            #包含当前值时，再试探下一个值
            self.backtrack(arr,target-arr[index],seq,index+1)
            seq.pop()
            #不包含当前值时，再试探下一个值
            self.backtrack(arr,target,seq,index+1)
        else:#如果超出target,则试探下一个值
            self.backtrack(arr,target,seq,index+1)


arr=[4,-4,2,1,4,-2,1,3]
comp=Composition()
print(comp.combinationSum(arr,6))
# comp.compose(arr,6)
# print(comp.combinationSum2(arr,6))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       