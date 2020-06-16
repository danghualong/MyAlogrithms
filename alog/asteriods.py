class Solution(object):
    def asteroidCollision(self, asteroids):
        result=[]
        if(asteroids==None or len(asteroids)==0):
            return result
        for i in range(len(asteroids)):
            # result为空时，就直接添加
            # result中的所有都往左走，则直接添加
            if(len(result)==0 or result[len(result)-1]<0):
                result.append(asteroids[i])
                continue
            # 当前asteriod向右，则直接加入
            if(asteroids[i]>0):
                result.append(asteroids[i])
            else:
                # 是否要添加当前卫星
                canAdd=True
                while(len(result)>0):
                    if(result[len(result)-1]<0):
                        break
                    # 撞碎result中的一个
                    if(result[len(result)-1]<-asteroids[i]):
                        result.pop()
                    elif(result[len(result)-1]==-asteroids[i]):
                        result.pop()
                        canAdd=False
                        break
                    else:
                        # 相向而行，但是result大于asteroid中的
                        canAdd=False
                        break
                if(canAdd):
                    result.append(asteroids[i])
        return result
            
    

obj=Solution()
result=obj.asteroidCollision([-2,-2,1,-2])
print(result)
        