# 多项式求和
def calc(cs,num):
    t=cs[0]
    for i in range(1,len(cs)):
        t=t*num+cs[i]
    return t


cs=[3,2,4,1]
t=calc(cs,2)
print(t)