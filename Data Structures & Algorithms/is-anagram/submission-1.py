class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list(s)
        s_list.sort()#sorting the list
        s_set=set(s_list)
        s_freq=[]
        for i in s_set:#iterating through the distinct values
            s_freq.append(int(s_list.count(i)))
        t_list=list(t)
        t_list.sort()#sorting the list
        t_set=set(t_list)
        t_freq=[]
        for i in t_set:#iterating through the distinct values
            t_freq.append(int(t_list.count(i)))
        if((s_set==t_set) and (s_freq==t_freq)):
            return True
        else:
            return False
