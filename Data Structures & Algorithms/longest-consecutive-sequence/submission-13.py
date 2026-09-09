#optimal solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxlength=0
        for n in numset:
            if(n-1 in numset):
                continue
            else:#start of a series
                count=1
                add=1
                while((n+add) in numset):
                    count+=1
                    add+=1
                maxlength=max(maxlength,count)
        return maxlength
        