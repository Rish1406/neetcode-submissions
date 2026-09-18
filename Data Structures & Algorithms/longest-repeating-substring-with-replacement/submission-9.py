#youtube video:https://www.youtube.com/watch?v=tkNWKvxI3mU&t=3s
#commented out code does not use dictionary, hence slower time compexity
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l=0
        # counts=[0]*26#to keep count of frequency of each alphabet
        # longest=0
        # for r in range(len(s)):
        #     counts[ord(s[r])-65]+=1#incrementing frequency of current alphabet
        #     while((r-l+1)-max(counts))>k:#reducing sliding window
        #         counts[ord(s[l])-65]-=1
        #         l+=1
        #     longest=max(longest,r-l+1)
        # return longest
        counts=defaultdict(int)
        l=0
        longest=0
        for r in range(len(s)):
            counts[s[r]]+=1
            while((r-l+1)-max(counts.values()))>k:
                counts[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest


        
        