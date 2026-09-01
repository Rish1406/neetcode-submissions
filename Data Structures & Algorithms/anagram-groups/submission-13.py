from collections import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)#automatically assigns default value to a key when you try to access or modify a key that does not exist. Default value assigned to a key in this line is a "List"
        for word in strs:
            count=[0]*26 #to keep a count of the frequency of each of the alphabet in the word
            for c in word:
                count[ord(c)-ord('a')]+=1#keeping track of frequency of the alphabets
            res[tuple(count)].append(word)
        return list(res.values())
