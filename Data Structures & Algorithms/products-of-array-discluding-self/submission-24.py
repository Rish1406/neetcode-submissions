class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        res=[]
        for n in nums:
            res.append(prod)
            prod*=n
        prod=1
        i=1
        l=len(nums)
        for n in nums[::-1]:
            res[l-i]*=prod
            prod*=n
            i+=1

        return res
        