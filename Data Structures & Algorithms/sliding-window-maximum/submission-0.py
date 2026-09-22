from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r=0,0#indexes of the window
        dq=deque()#stores of the index and not the numbers in the index
        res=[]
        while r<len(nums):
            while dq and nums[dq[-1]]<nums[r]:#makign sure the deque is a decreasing monotonic
                dq.pop()
            dq.append(r)
        
            if l>dq[0]:#this helps to remove index that are not within the current window and hence is why deque stores the index alone 
                dq.popleft()
        
            if(((r-l)+1)%k==0):
                res.append(nums[dq[0]])#leftmost of deque is the highest value
                l+=1
            r+=1
        return res


