
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if(x<y):
            x,y=y,x
        if(x<0):
            return False
        else:
            if(y<0):
                return x==z
            elif(y==0):
                return (x==z or y==z)
            else:
                if(x==z or y==z or x+y==z):
                    return True
        t=x
        mod=0
        while(True):
            t-=y
            print(x,y,t,mod)
            if(t==z):
                return True
            if(t<y):
                mod=t
                if(x+t==z):
                    return True
                t=x+mod
                if(mod==0):
                    break
        return False

x,y,z=(3,5,4)
print(Solution().canMeasureWater(x,y,z))