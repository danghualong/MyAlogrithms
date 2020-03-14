# 递归求解最长公共子序列
def calc(a,b,m,n):
    if(m==-1 or n==-1):
        return 0
    if(a[m]==b[n]):
        return calc(a,b,m-1,n-1)+1
    else:
        len1=calc(a,b,m-1,n)
        len2=calc(a,b,m,n-1)
        return len1 if len1>len2 else len2


a=['a','s','d','b','t','c']

b=['a','b','s','d','t','c','g']

mylen=calc(a,b,5,5)
print(mylen)
