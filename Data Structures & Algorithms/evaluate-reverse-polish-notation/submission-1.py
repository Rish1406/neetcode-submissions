class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char.lstrip("-").isdigit():
                stack.append(int(char))
            else:
                val2=stack.pop()
                val1=stack.pop()
                if char=="+":
                    stack.append(val1+val2)
                elif char=="-":
                    stack.append(val1-val2)
                elif char=="*":
                    stack.append(val1*val2)
                else:
                    stack.append(int(val1/val2))
            # print(stack)
        return stack[-1]
        