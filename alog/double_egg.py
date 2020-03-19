
import math
# 动态规划实现双蛋问题
def calc(m,n):
    arr=[[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        arr[i][0]=i+1
    for j in range(n):
        arr[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            minNum=math.inf
            for k in range(i):
                # if the egg is not broken
                t1=1+arr[i-1-k][j]
                # if the egg is broken
                t2=arr[k][j-1]
                # get the maximum
                num=t1 if t1>t2 else t2
                # get the minimum of the nums in different k
                if(num<minNum):
                    minNum=num
            arr[i][j]=minNum
    print(arr)
    


calc(100,20)