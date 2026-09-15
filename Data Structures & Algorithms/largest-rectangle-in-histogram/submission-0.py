class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        maxArea=0
        for i, n in enumerate(heights):
            pop_i=i
            while stk and stk[-1][1]>n:
                pop_i,pop_num=stk.pop()
                new_area=pop_num*(i-pop_i)
                # print(new_area)
                maxArea=max(new_area,maxArea)
            stk.append((pop_i,n))
        limit=len(heights)
        for i,n in stk:
            new_area=n*(limit-i)
            maxArea=max(new_area,maxArea)
        return maxArea

        