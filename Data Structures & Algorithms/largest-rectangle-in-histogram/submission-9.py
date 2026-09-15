#Logic from https://www.youtube.com/watch?v=ZGMw8Bvpwd4
#code done by own
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]#monotonic stack
        maxArea=0
        for i, n in enumerate(heights):
            pop_i=i#initialised here as pop_i changes within while loop at line 9, when current height can no longer be extended
            while stk and stk[-1][1]>n:
                pop_i,pop_num=stk.pop()
                new_area=pop_num*(i-pop_i)#it can be infered that pop_num can be extended till i since stack is monotonic(ascending order)
                maxArea=max(new_area,maxArea)
            stk.append((pop_i,n))
        limit=len(heights)
        for i,n in stk:#to measure area of the remaining elements in the stack. The remaining elements in the stack are the ones that can be extended till the last index
            new_area=n*(limit-i)
            maxArea=max(new_area,maxArea)
        return maxArea

        