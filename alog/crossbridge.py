
#递归求解过河问题
class Solution(object):
    def __init__(self):
        self.paths=[]

    def crossBridge(self,arr,n):
        if(n==0):
            return 0
        elif(n==1):
            self.paths.append("---->0")
            return arr[0]
        elif(n==2):
            self.paths.append("-->0,1")
            return arr[1]
        elif(n==3):
            self.paths.append("-->0,1")
            self.paths.append("<----0")
            self.paths.append("-->0,2")
            return arr[0]+arr[1]+arr[2]
        else:
            #最快的和次快的先过，最快的回来，让最慢的两个过去，次快的回来
            time1=arr[0]+2*arr[1]+arr[n-1]
            #最快的把两个最慢的先后送过去，再回来
            time2=2*arr[0]+arr[n-1]+arr[n-2]
            #取以上两种方案时间最短的
            if(time1<time2):
                self.paths.append("-->0,1")
                self.paths.append("<----0")
                self.paths.append("-->{0},{1}".format(n-2,n-1))
                self.paths.append("<----1")
            else:
                self.paths.append("-->0,{0}".format(n-1))
                self.paths.append("<----0")
                self.paths.append("-->0,{0}".format(n-2))
                self.paths.append("<----0")
            time=time1 if time1<time2 else time2
            return time+self.crossBridge(arr,n-2)

#从小到大排序
arr=[1,4,5,6,9,12]
s=Solution()
print(s.crossBridge(arr,len(arr)))
for i in range(len(s.paths)):
    print(s.paths[i])

            
