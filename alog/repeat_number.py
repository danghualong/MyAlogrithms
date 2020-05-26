# t1:初始点到环形入口点的距离
# t2:二者相遇的点，距离环形入口点的距离
# n:不同数值的量
# 2(t1+t2)-(t1+t2)=(n-t1)*k
# t2=(n-t1)*k-t1 
def findRepeatNumber(nums):
    slow=0
    quick=0
    slowList=[slow]
    quickList=[quick]
    while(True):
        slow=nums[slow]
        quick=nums[nums[quick]]
        slowList.append(slow)
        quickList.append(quick)
        if(slow==quick):
            break
    print(slowList)
    print(quickList)
    slow=0
    while(slow!=quick):
        slow=nums[slow]
        quick=nums[quick]
        print(slow,quick)
    return(slow)

nums=[1,3,3,2,3]
print(findRepeatNumber(nums)) 

nums=[2,5,9,6,9,3,8,9,7,1]
print(findRepeatNumber(nums)) 

