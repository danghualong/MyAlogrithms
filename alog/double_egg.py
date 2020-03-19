
import math
# 动态规划实现双蛋问题
def calc(m,n):
    arr=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        arr[i][1]=i
    for j in range(1,n+1):
        arr[1][j]=1
    for i in range(2,m+1):
        for j in range(2,n+1):
            minNum=math.inf
            for k in range(i):
                # if the egg is not broken
                t1=arr[i-k-1][j]
                # if the egg is broken
                t2=arr[k][j-1]
                # print('i:{2},j:{3},k:{4},t1:{0},t2:{1}'.format(t1+1,t2+1,i,j,k))
                    
                # get the maximum
                num=t1 if t1>t2 else t2
                num+=1
                # get the minimum of the nums in different k
                if(num<minNum):
                    minNum=num
            arr[i][j]=minNum
    print(arr)
    


calc(100,10)