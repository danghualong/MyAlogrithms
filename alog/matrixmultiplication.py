import math

def times(arr):
    n=len(arr)
    s=[]
    result=[]
    for i in range(n):
        s.append([])
        result.append([])
        for j in range(n):
            s[i].append(0)
            result[i].append(0)
    for i in range(1,n):
        for j in range(n-i-1,-1,-1):
            r=n-1-j-i
            c=n-1-j
            minV=math.inf
            mid=0
            for h in range(i):
                t=s[r][r+h]+s[r+h+1][c]+arr[r][0]*arr[r+h][1]*arr[c][1]
                if(t<minV):
                    mid=r+h
                    minV=t
            result[r][c]=mid
            s[r][c]=minV
    print(s) 
    print(result)

arr=[[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]
times(arr)