class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        res=[1]
        for i in range(len(nums)-1):
            prefix*=nums[i]
            res.append(prefix)
        postfix=1
        for i in range(len(nums)-1,-1,-1):#going backwards
            res[i]*=postfix
            postfix*=nums[i]
        return res
    
            