import numpy as np
# 动态规划算法
# 查找任意多个数值的和等于目标值的组合
# 每个数可以使用多次
class Solution(object):
    def __init__(self,types,target):
        self.types=types
        self.target=target
        m=len(types)
        self.arr=np.zeros((m+1,target+1))

    def solve(self):
        m=len(self.types)
        n=self.target
        # 每个组成的序列 共（m*n)个
        seqs=[[None for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            # 当前币的面额
            c=self.types[i-1]
            for j in range(1,n+1):
                if(j<c):# 当总额小于面值时
                    self.arr[i][j]=self.arr[i-1][j]
                    # 深度拷贝序列
                    seqs[i][j]=deepcopy(seqs[i-1][j]) 
                # 当总额刚好等于面值时
                elif(j==c):
                    self.arr[i][j]=self.arr[i-1][j]+1
                    # 深度拷贝序列,同时增加一个序列
                    seqs[i][j]=deepcopy(seqs[i-1][j])
                    seqs[i][j].append([c])          
                else: # 当总额大于面值时
                    self.arr[i][j]=self.arr[i][j-c]+self.arr[i-1][j]
                    # 深度拷贝序列
                    seqs[i][j]=deepcopy(seqs[i-1][j])
                    # 左侧的序列要增加一个元素
                    tmp=deepcopy(seqs[i][j-c])
                    for seq in tmp:
                        seq.append(c)
                    # 合并两个序列
                    seqs[i][j].extend(tmp)
        return self.arr[1:,1:],seqs

def deepcopy(src):
    dst=[]
    if(src==None or len(src)==0):
        return dst
    for k in src:
        dst.append(k.copy())
    return dst


if __name__=='__main__':                
    target=14
    types=[1,2,5,8]
    s=Solution(types,target)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    result,seqs=s.solve()
    # 添加头部
    headers=np.arange(1,target+1).reshape(1,-1)
    result=np.concatenate((headers,result),axis=0)
    print('use {0} to compose the target result:'.format(types))
    print(result)
    print("the seqence to {0} are:".format(target))
    print(seqs[len(types)][target])

