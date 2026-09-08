from collections import *
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if(diff in hashMap):
                if(i<hashMap[diff]):
                    return [i+1,hashMap[diff]+1]
                else:
                    return [hashMap[diff]+1,i+1]
            else:
                hashMap[numbers[i]]=i


        