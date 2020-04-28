import math
# 鳄鱼岛逃生问题
# 
def race(vb,vs,r):
    d=math.pi*0.05
    k=r*d*vs/vb
    distance=k
    distance_list=[]
    distance_list.append(distance)
    times=1
    resolved=True
    while(distance<(1-vs*math.pi/vb)*r):
        tmp=distance*math.sin(d)
        # 此处不应该出现这种情况
        if(k<tmp):
            resolved=False
            break
        distance=distance*math.cos(d)+math.sqrt(k**2-tmp**2)
        if(distance<=distance_list[len(distance_list)-1]):
            resolved=False
            break
        distance_list.append(distance)
        times+=1
    if(resolved):
        print(distance_list)    
        print(times)
    

if __name__=='__main__':
    race(4,1,20)