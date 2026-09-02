from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq=Counter(nums)#this is a dictionary with value:freq
        temp=list(freq.values())#getting all the frequencies
        temp.sort(reverse=True)#sorting in descending order so the first element is the most frequent
        check=temp[0:k]#list that contains the k most frequncies
        for num in check:
            for key,value in freq.items():
                if num==value:
                    res.append(key)
                    freq.pop(key)
                    break
        return res





        