
import math
import numpy as np

# 动态规划实现双蛋问题
def calc(m,n):
    arr=np.zeros((m+1,n+1))
    arr[1,1:]=1
    arr[:,1]=np.arange(m+1)
    for i in range(2,m+1):
        for j in range(2,n+1):
            minNum=math.inf
            for k in range(1,i+1):
                # 在第k层抛第一蛋
                # 如果蛋碎了
                t1=arr[k-1][j-1]
                # 如果蛋没有碎
                t2=arr[i-k][j]
                # 取两种情况的最大值
                num=t1 if t1>t2 else t2
                num+=1
                # 然后取0-i层中，取次数最少的
                if(num<minNum):
                    minNum=num
            arr[i][j]=minNum
    print(arr[1:,1:])


if __name__=="__main__":
    calc(100,10)