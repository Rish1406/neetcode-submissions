#Logic from https://www.youtube.com/watch?v=ZGMw8Bvpwd4
#code done by own
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]#monotonic stack
        maxArea=0
        for i, n in enumerate(heights):
            pop_i=i#initialised here as pop_i will change if the current height can no longer be extended
            while stk and stk[-1][1]>n:#checking if stack is not empty and the current height is lesser than the top height of stack(i.e the top height of stack can no longer be extended). Note the while loop used
                pop_i,pop_num=stk.pop()
                new_area=pop_num*(i-pop_i)
                maxArea=max(new_area,maxArea)
            stk.append((pop_i,n))
        limit=len(heights)
        for i,n in stk:#to measure area of the remaining elements in the stack. The remaining elements in the stack are the ones that can be extended till the last index
            new_area=n*(limit-i)
            maxArea=max(new_area,maxArea)
        return maxArea

        