#Youtube video:https://www.youtube.com/watch?v=B1k_sxOSgv8. Logic taken from here but code is my own
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            encoded+=str(len(s))+"#"+s
        return encoded


    def decode(self, s: str) -> List[str]:
        i=0
        decoded=[]
        while i<len(s):
            index_of_del=s.find("#",i+1)#finding the index of the delimiter and using (i+1) as the start of the search.
            word_len=int(s[i:index_of_del])#getting the length of the word
            word=s[index_of_del+1:index_of_del+word_len+1]#Fetching the word
            decoded.append(word)#Appending the word to the list
            i=index_of_del+word_len+1#resetting i to the index just after the word
        return decoded

