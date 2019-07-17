class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i=0;j=len(nums1)-1
        k=0;l=len(nums2)-1
        while(True):
            if(j-i+l-k<1):
              #  print(i,j,k,l)
                if(j-i==1):
                    return float(nums1[j]+nums1[i])/2
                if(l-k==1):
                    return float(nums2[k]+nums2[l])/2
                if(j-i==0):
                    if(l-k==0):
                        return float(nums1[i]+nums2[k])/2
                    return nums1[j]
                if(l-k==0):
                    return nums2[k]
            if (j-i<0):
                k+=1
            elif (l-k<0):
                i+=1
            else:    
                if(nums1[i]>nums2[k]):
                    k+=1
                else:
                    i+=1
            if(j-i<0):
                    l-=1
            elif(l-k<0):
                    j-=1
            else:  
                if(nums1[j]>nums2[l]):
                    j-=1
                else:
                    l-=1
        
            
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        