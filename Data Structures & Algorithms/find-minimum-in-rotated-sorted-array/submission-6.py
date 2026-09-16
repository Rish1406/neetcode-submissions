import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        while nums[l]>nums[r]:
            mid=(l+r)//2
            if(nums[mid]>=nums[l]):
                l=mid+1
            else:
                res=min(res,nums[mid])
                r=mid-1
        if l<=r:
            res=min(res,nums[l])
        return res

        