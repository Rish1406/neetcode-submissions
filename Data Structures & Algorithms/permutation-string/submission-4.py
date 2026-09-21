from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1_map=defaultdict(int)
        # s2_map=defaultdict(int)
        # for c in s1:
        #     s1_map[c]+=1
        # l=0
        # r=len(s1)-1
        # while r<len(s2):
        #     for c in s2[l:r+1]:
        #         s2_map[c]+=1
        #     if s1_map==s2_map:
        #         return True
        #     s2_map.clear()
        #     l+=1
        #     r+=1
        # return False
        n1,n2=len(s1),len(s2)
        s1_map=Counter(s1)
        s2_map=Counter(s2[:n1])

        if s1_map==s2_map:
            return True
        
        for i in range(n1,n2):
            s2_map[s2[i]]+=1#sliding window
            s2_map[s2[i-n1]]-=1
            if s1_map==s2_map:
                return True
        
        return False



