import numpy as np

class Solution(object):
    def __init__(self,types,target):
        self.types=types
        self.target=target
        m=len(types)
        self.arr=[[0 for j in range(target+1)] for i in range(m)]

    def solve(self):
        m=len(self.types)
        s=self.target
        for t in range(m):
            if(t==0):
                for i in range(1,s+1):
                    if(self.target%self.types[t]==0):
                        self.arr[t][i]=1
            else:
                for i in range(1,s+1):
                    if(i>self.types[t]):
                        self.arr[t][i]=self.arr[t-1][i]+self.arr[t][i-self.types[t]]
                    elif(i==self.types[t]):
                        self.arr[t][i]=self.arr[t-1][i]+1
                    else:
                        self.arr[t][i]=self.arr[t-1][i]
        for i in range(m):               
            print(self.arr[i])
        
                

s=Solution([1,2,5],8)
s.solve()

