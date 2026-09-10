class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={")":"(","}":"{","]":"["}
        stack=[]
        for char in s:
            if char in hashMap:#checking if character is a closing bracket
                if stack and stack[-1]==hashMap[char]:#checking is stack is empty(we cannot add a closing bracket to an empty stack) and checking if top of stack is opening bracket of "char"
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack)==0


        