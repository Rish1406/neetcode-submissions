class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        target=0
        for index,a in enumerate(nums):
            if index>0 and nums[index]==nums[index-1]:
                continue
            i,j=index+1,len(nums)-1
            while i<j:
                sum=a+nums[i]+nums[j]
                if(sum<target):
                    i+=1
                elif(sum>target):
                    j-=1
                else:
                    res.append([a,nums[i],nums[j]])
                    i+=1
                    while(nums[i]==nums[i-1] and i<j):
                        i+=1
        return res

        