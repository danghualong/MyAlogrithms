import numpy as np
import random as rand
import matplotlib.pyplot as plt


def getRandList(m,n):
    list=[i for i in range(n)]
    rand.shuffle(list)
    return list[:m]



def getTestResult(target,m,n):
    pool=getRandList(m,n)
    # print(target)
    # print(pool)
    for i in range(len(target)):
        if(i not in pool):
            return False
    return True

def getPoss(times,k,m,n):
    target=getRandList(k,n)
    size=0
    for i in range(times):
        size+=1 if getTestResult(target,m,n) else 0
    return size/times

if __name__=="__main__":
    groups=100
    times=10000
    k=5
    m=9
    n=11

    y=[]
    for i in range(groups):
        y.append(getPoss(times,k,m,n))
    x=[i for i in range(groups)]
    plt.plot(x,y)
    plt.show()


        
        


    