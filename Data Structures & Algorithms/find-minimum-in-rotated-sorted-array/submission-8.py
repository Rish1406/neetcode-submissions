class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        while nums[l]>nums[r]:#if array is rotated
            mid=(l+r)//2
            if(nums[mid]>=nums[l]):
                l=mid+1#shift search to right 
            else:
                res=min(res,nums[mid])
                r=mid-1#shift search to left
        if l<=r:#array or subarray in ascending order
            res=min(res,nums[l])
        return res

        