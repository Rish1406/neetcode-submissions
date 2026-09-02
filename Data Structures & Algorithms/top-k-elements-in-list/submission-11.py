#Optimal Solution
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=dict(Counter(nums))
        bucket_sort=[[] for i in range(len(nums)+1)]
        for n,c in freq.items():
            bucket_sort[c].append(n)#if number occurs c times, it is added to the list at c index of bucket_sort
            res=[]
        for i in range(len(nums),0,-1):
            for n in bucket_sort[i]:
                res.append(n)
                k-=1
            if k==0:
                return res
            