#Fundamental idea: min(LeftBoundary,RightBoundary)-height[i]
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1#defining the left and right pointer
        maxLeft,maxRight=height[l],height[r]
        res=0
        while l<r:
            if(maxLeft<maxRight):#that is if left boundary is minimum
                l+=1
                temp=maxLeft-height[l]
                if(temp>-1):#If positive
                    res+=temp
                maxLeft=max(maxLeft,height[l])
            else:#this if right boundary is minimum or both are equal(if maxLeft and maxRight are equal, it does not matter if you shift l or r)
                r-=1
                temp=maxRight-height[r]
                if(temp>-1):#If positive
                    res+=temp
                maxRight=max(maxRight,height[r])
        return res




            
                    

        
        