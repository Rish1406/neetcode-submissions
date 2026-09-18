#youtube video:https://www.youtube.com/watch?v=tkNWKvxI3mU&t=3s
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        counts=[0]*26#to keep count of frequency of each alphabet
        longest=0
        for r in range(len(s)):
            counts[ord(s[r])-65]+=1#incrementing frequency of current alphabet
            while((r-l+1)-max(counts))>k:#reducing sliding window
                counts[ord(s[l])-65]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest

        
        