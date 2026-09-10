class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        while i<len(s):
            if not stack:
                stack.append(s[i])
            else:
                current=ord(s[i])
                topofstack=ord(stack[-1])
                diff=current-topofstack
                if diff==1 or diff==2:
                    stack.pop()
                else:
                    stack.append(s[i])
            i+=1
        if not stack:
            return True
        else:
            return False

