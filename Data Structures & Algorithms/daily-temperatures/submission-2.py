#Use a Monotonic stack
#youtube video: https://www.youtube.com/watch?v=_ZEvmycwXHs
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        monostack=[]
        for i,t in enumerate(temperatures):
            while monostack and monostack[-1][0]<t:#while stack is not empty and temperature on top of stack is less than current temperature
                stk_t,stk_i=monostack.pop()
                res[stk_i]=i-stk_i
            monostack.append((t,i))
        return res


        