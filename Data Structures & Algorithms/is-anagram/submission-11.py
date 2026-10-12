from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_list=list(s)
        # t_list=list(t)
        if(Counter(s)==Counter(t)):
            return True
        else:
            return False