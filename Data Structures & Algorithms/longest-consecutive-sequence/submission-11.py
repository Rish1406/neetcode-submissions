#optimal solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numset=set(nums)
        # maxCount=0
        # for n in numset:
        #     if(n-1 in numset):
        #         continue
        #     else:#start of a series
        #         count=1
        #         add=1
        #         while((n+add) in numset):
        #             count+=1
        #             add+=1
        #         maxCount=max(maxCount,count)
        # return maxCount
        numset=set(nums)
        longest=0
        for n in numset:
            if (n-1) not in numset:
                length=0
                while((n+length) in numset):
                    length+=1
                longest=max(longest,length)
        return longest
        