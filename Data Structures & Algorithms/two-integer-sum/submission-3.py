class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using hasmap
        prevMap={}#dictionary of val:index
        for i,value in enumerate(nums):
            diff=target-value
            if diff in prevMap:#in function when used, goes through the dictionary's keys by default
                return [prevMap[diff],i]
            prevMap[value]=i
        return []

