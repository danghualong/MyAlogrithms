import numpy as np

#编辑距离计算

def distance_sub(s1,i,s2,j):
    if(i==-1):
        return j+1
    if(j==-1):
        return i+1
    if(s1[i]==s2[j]):
        return distance_sub(s1,i-1,s2,j-1)
    else:
        d1=distance_sub(s1,i,s2,j-1)+1
        d2=distance_sub(s1,i-1,s2,j)+1
        d3=distance_sub(s1,i-1,s2,j-1)+1
        return min(d1,d2,d3)
# 递归求解
def reccursive_distance(s1,s2):
    return distance_sub(s1,len(s1)-1,s2,len(s2)-1)
# 动态规划求解
def dp_distance(s1,s2):
    row=len(s1)+1
    col=len(s2)+1
    d=np.zeros((row,col))
    for i in range(1,row):
        d[i,0]=i
    for j in range(1,col):
        d[0,j]=j
    for i in range(1,row):
        for j in range(1,col):
            if(s1[i-1]==s2[j-1]):
                d[i,j]=d[i-1,j-1]
            else:
                d1=d[i,j-1]+1 #增加一个字符
                d2=d[i-1,j]+1 #删除一个字符
                d3=d[i-1,j-1]+1 #修改一个字符
                d[i,j]=min(d1,d2,d3)
    print(d[1:,1:])



    
s1='rap'
s2='apple'
print(reccursive_distance(s1,s2))

dp_distance(s1,s2)
