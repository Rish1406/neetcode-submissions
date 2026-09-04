from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list(s)
        t_list=list(t)
        print(Counter(s_list),Counter(t_list))
        if(Counter(s_list)==Counter(t_list)):
            return True
        else:
            return False