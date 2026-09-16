class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l,r=0,m-1
        while l<=r:
            mid=(l+r)//2
            if(matrix[mid][0]<=target and matrix[mid][n-1]>=target):
                l1,r1=0,n-1
                while l1<=r1:
                    mid1=(l1+r1)//2
                    if matrix[mid][mid1]==target:
                        return True
                    elif matrix[mid][mid1]>target:
                        r1=mid1-1
                    else:
                        l1=mid1+1
                return False
            elif(matrix[mid][0]>target):
                r=mid-1
            elif(matrix[mid][n-1]<target):
                l=mid+1
        return False
    
