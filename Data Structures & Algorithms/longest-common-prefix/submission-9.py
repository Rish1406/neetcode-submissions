class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]#consider the first string in the list as prefix
        for i in range(len(prefix)):
            for word in strs:
                if i==len(word) or word[i]!=prefix[i]:
                    return prefix[:i]#up until i, excluding i
        return prefix
                

            

