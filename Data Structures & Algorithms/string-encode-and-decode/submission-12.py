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
            index_of_del=s.find("#",i+1)
            word_len=int(s[i:index_of_del])#(i+1) is the index to start search
            word=s[index_of_del+1:index_of_del+word_len+1]
            decoded.append(word)
            i=index_of_del+word_len+1
        return decoded

