#Solutiom 1 is more easier way of understanding, can be further optimised to this code
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1#defining the left and right pointer
        maxLeft,maxRight=height[l],height[r]
        res=0
        while l<r:
            if(maxLeft<maxRight):#that is if left boundary is minimum
                l+=1
                maxLeft=max(maxLeft,height[l])
                res+=maxLeft-height[l]#Will never be 0
            else:#if right boundary is minimum or both are equal(if maxLeft and maxRight are equal, it does not matter if you shift l or r)
                r-=1
                maxRight=max(maxRight,height[r])
                res+=maxRight-height[r]
        return res
        