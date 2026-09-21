from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        s1_map=Counter(s1)
        s2_map=Counter(s2[:n1])

        if s1_map==s2_map:
            return True
        
        for i in range(n1,n2):
            s2_map[s2[i]]+=1#sliding window addition of character
            s2_map[s2[i-n1]]-=1#sliding window removal of character
            if s1_map==s2_map:#even though this takes 0(k) times, since k here is fixed alphabet sizes, it is taken as 0(1), a constant
                return True
        
        return False



