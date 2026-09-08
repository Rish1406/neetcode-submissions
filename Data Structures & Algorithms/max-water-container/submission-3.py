#We use 2 pointers at extreme left and extreme right as we want to maximise the width. we shift based on the one with the max height as we want the maximum area off container

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        i=0
        j=len(heights)-1
        while i<j:
            area=(j-i)*min(heights[i],heights[j])
            max_area=max(max_area,area)
            if(heights[i]>heights[j]):
                j-=1
            elif(heights[i]<heights[j]):
                i+=1
            else:
                i+=1
        return max_area

        
        