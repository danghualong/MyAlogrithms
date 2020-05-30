

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if(nums1==None and nums2==None):
            return None
        if(len(nums1)==0 and len(nums2)==0):
            return None
        elif(len(nums1)>0 and len(nums2)==0):
            return self.getMedianForSingleArray(nums1)
        elif(len(nums1)==0 and len(nums2)>0):
            return self.getMedianForSingleArray(nums2)
        else:
            size1=len(nums1)
            size2=len(nums2)
            if((size1+size2)%2!=0):
                result=self.getSortNumber(nums1,nums2,int((size1+size2-1)/2))
            else:
                t1=self.getSortNumber(nums1,nums2,int((size1+size2)/2-1))
                t2=self.getSortNumber(nums1,nums2,int((size1+size2)/2))
                result=(t1+t2)/2.0
            return result
    
    def getSortNumber(self,nums1,nums2,k):
        size1=len(nums1)
        size2=len(nums2)
        curIndex1=0
        curIndex2=0
        while(curIndex1+curIndex2<k):
            print(curIndex1,curIndex2,k)
            halfK=int((k-curIndex1-curIndex2)/2)-1
            if(halfK<0):
                halfK=0
            if(curIndex1+halfK>size1):
                return nums2[k-size1]
            elif(curIndex1+halfK==size1):
                curIndex1=size1-1
            if(curIndex2+halfK>size2):
                return nums1[k-size2]
            elif(curIndex2+halfK==size2):
                curIndex2=size2-1
            
            if(nums1[curIndex1+halfK]>nums2[curIndex2+halfK]):
                curIndex2=curIndex2+halfK+1
            else:
                curIndex1=curIndex1+halfK+1
        if(curIndex1>=size1):
            return nums2[curIndex2]
        elif(curIndex2>=size2):
            return nums1[curIndex1]
        else:
            result= min(nums1[curIndex1],nums2[curIndex2])
            return result

    def getMedianForSingleArray(self,nums):
        if(nums==None or len(nums)==0):
            return None
        size=len(nums)
        if(size%2==0):
            return (nums[int(size/2-1)]+nums[int(size/2)])/2.0
        else:
            return float(nums[int((size-1)/2)])
                




nums1=[5]
nums2=[1,2,3,4,6,7,8]
obj=Solution()
result=obj.findMedianSortedArrays(nums1,nums2)
print(result)