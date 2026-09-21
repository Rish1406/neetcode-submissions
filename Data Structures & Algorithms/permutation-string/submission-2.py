from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map=defaultdict(int)
        s2_map=defaultdict(int)
        for c in s1:
            s1_map[c]+=1
        l=0
        r=len(s1)-1
        while r<len(s2):
            for c in s2[l:r+1]:
                s2_map[c]+=1
            if s1_map==s2_map:
                return True
            s2_map.clear()
            l+=1
            r+=1
        return False

