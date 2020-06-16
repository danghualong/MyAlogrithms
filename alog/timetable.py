class Node(object):
    def __init__(self,val):
        self.val=val
        self.prev=[]
        self.next=[]

class TimeTable(object):
    def canFinish(self, numCourses, prerequisites):
        nodes={}
        for item in prerequisites:
            if(item[0] not in nodes):
                nodes[item[0]]=Node(item)
            if(item[1] not in nodes):
                nodes[item[1]]=Node(item[1])
            nodes[item[0]].prev.append(nodes[item[1]])
            nodes[item[1]].next.append(nodes[item[0]])
        while(True):
            deleted=False
            for key in list(nodes.keys()):
                if(len(nodes[key].prev)==0):
                    for i in range(len(nodes[key].next)-1,-1,-1):
                        item=nodes[key].next[i]
                        item.prev.remove(nodes[key])
                    nodes.pop(key)
                    deleted=True
            if(not deleted):
                break
        return len(nodes)==1

    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if(k==0):
            return []
        
        tmp=set([0])
        for i in range(k):
            result=set()
            for item in tmp:
                result.add(item+shorter)
                result.add(item+longer)
            print((1956 in result),(1958 in result))
            tmp=result.copy()
        return list(result)
    
    def findLeastNumOfUniqueInts(self, arr, k):
        if(arr==None or len(arr)==0):
            return 0
        if(k>=len(arr)):
            return 0
        dict={}
        for t in arr:
            if(t not in dict):
                dict[t]=0
            dict[t]+=1
        if(k<=0):
            return len(dict)
        nums=[]
        for key in dict:
            nums.append(dict[key])
        nums.sort()
        s=0
        startIndex=0
        for i in range(len(nums)):
            s+=nums[i]
            if(s>k):
                startIndex=i
                break
        return len(nums)-i

    def minDays(self, bloomDay, m, k):            
        if(m<=0 or k<=0 or bloomDay==None or len(bloomDay)==0):
            return -1
        if(len(bloomDay)<m*k):
            return -1
        tmpTypes=set()
        for d in bloomDay:
            tmpTypes.add(d)
        dayTypes=list(tmpTypes)
        dayTypes.sort()
        print(dayTypes)
        for day in dayTypes:
            stack=[-1]
            for i in range(len(bloomDay)):
                if(bloomDay[i]-day>0):
                    stack.append(i)
            stack.append(len(bloomDay))
            print(bloomDay,stack)
            size=self.countFlowers(stack,k)
            if(size>=m):
                return day
        return -1                                                                                                                                                                                                   
                


    def countFlowers(self,stack,k):
        size=0
        for i in range(len(stack)-1):
            size+=((stack[i+1]-stack[i]-1)//k)
        return size
                
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        if(arr==None or len(arr)==0):
            return -1
        n=len(arr)
        dict={}
        nums=[]
        s=0
        maxNum=arr[0]
        for i in range(n):
            s+=arr[i]
            if(arr[i]>maxNum):
                maxNum=arr[i]
            if(arr[i] not in dict):
                dict[arr[i]]=0
                nums.append(arr[i])
            dict[arr[i]]+=1
        if(s<=target):
            return maxNum
        nums.sort()
        diff=s-target
        result=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            s-=((nums[i+1]-nums[i])*dict[nums[i+1]])
            if(abs(s-target)<diff):
                diff=abs(s-target)
                result=nums[i]
            else:
                break
        return result      


    def findBestValue2(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        if(arr==None or len(arr)==0):
            return -1
        n=len(arr)
        arr.sort()
        s=0
        for i in range(n):
            t=(target-s)//(n-i)
            if(t<arr[i]):
                dt=float(target-s)/(n-i)
                if(dt-t>0.5):
                    return t+1
                else:
                    return t
            s+=arr[i]
        return arr[n-1]                   
        


        

obj=TimeTable()
# result=obj.canFinish(3,[[0,1],[1,2],[1,3]])
# print(result)

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

# result2=obj.minDays(bloomDay,m,k)

# print(result2)

#  result2=obj.findBestValue(bloomDay,m,k)    

result2=obj.findBestValue2([60864,25176,27249,21296,20204],56803)
print(result2)      

               


